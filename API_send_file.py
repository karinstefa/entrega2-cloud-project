from flask import Flask
from flask import request
import boto3
import base64


app = Flask(__name__)

folder = 'test/'


@app.route('/users', methods=['POST'])
def user():
    if request.method == 'POST':
        data = request.get_json()

        file_voice = data['file_voice']
        file_bs64 = data['file_bs64']
        file_name_with_extention = f'{folder}{file_voice}'

        s3 = boto3.client('s3')
        msg = base64.b64decode(file_bs64)
        s3.put_object(Body=msg, Bucket="test-bucket-cloud-1",
                      Key=file_name_with_extention)

        # Create SQS client
        sqs = boto3.client('sqs', region_name='us-east-1')
        # %%
        queue_url = 'https://sqs.us-east-1.amazonaws.com/734030550837/test.fifo'
        # %%
        # Send message to SQS queue
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageAttributes={
                'File64': {
                    'DataType': 'String',
                    'StringValue': file_voice
                },
                'Filename': {
                    'DataType': 'String',
                    'StringValue': file_bs64
                }
            },
            MessageDeduplicationId='string',
            MessageGroupId="12",
            MessageBody=(
                'Documento listo'
            )
        )

        return ({
            'Sucess': 'True',
        })

    else:
        print('POST Error 405 Method Not Allowed')
        return ({'Sucess': 'False'})
