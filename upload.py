import boto3

s3 = boto3.client('s3')
with open("test.py", "rb") as f:
    s3.upload_fileobj(f, "test-bucket-cloud-1", "test")