#%%
import boto3

#%%
# Create SQS client
sqs = boto3.client('sqs',region_name='us-east-1')
#%%
queue_url = 'https://sqs.us-east-1.amazonaws.com/734030550837/test.fifo'
#%%
# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ]
)
#%%
print(response)
message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']
#%%

# Delete received message from queue

sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)

#%%
print('Received and deleted message: %s' % message)

