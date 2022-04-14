#%%
from email.message import Message
import boto3
#%%
# Create SQS client
sqs = boto3.client('sqs',region_name='us-east-1')
#%%
queue_url = 'https://sqs.us-east-1.amazonaws.com/734030550837/test.fifo'
#%%
# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageAttributes={
        'File64': {
            'DataType': 'String',
            'StringValue': 'The Whistler'
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        }
    },
    MessageDeduplicationId='string',
    MessageGroupId="12",
    MessageBody=(
        'Test 002 '
        'week of 12/11/2016.'
    )
)
#%%

print(response['MessageId'])
