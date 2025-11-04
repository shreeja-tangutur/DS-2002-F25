import boto3

s3 = boto3.client('s3', region_name='us-east-1')

bucket_name = 'ds2002-f25-ebz4sn'
local_file = 'brown_bear.jpg'

# 1. Upload the private file
with open(local_file, 'rb') as data:
    resp = s3.put_object(
        Body=data,
        Bucket=bucket_name,
        Key=local_file
    )

print(f"{local_file} uploaded privately to {bucket_name}.")

s3.upload_file(
    Filename=local_file,
    Bucket=bucket_name,
    Key='brown_bear_public.jpg',
    ExtraArgs={'ACL': 'public-read'}
)

print(f"{local_file} uploaded publicly as brown_bear_public.jpg.")
