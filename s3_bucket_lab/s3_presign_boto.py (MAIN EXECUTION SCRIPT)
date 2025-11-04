import boto3
import urllib.request
import os

gif_url = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXcyNXNsdGg0dW5uZmk0c2JrcW1wM3hvNGhiOWozYmlvaWI2YWp6bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fUYhyT9IjftxrxJXcE/giphy.gif"
local_upload =  "jerry.gif"
bucket_name = "ds2002-f25-ebz4sn"
object_name = local_upload
expires_in=604800

print(f"Getting GIF from URL")
urllib.request.urlretrieve(gif_url, local_upload)
print(f"File saved locally successfully")

s3 = boto3.client('s3', region_name ='us-east-1')

print(f"Uploading GIF to bucket {bucket_name}")
s3.upload_file(local_upload, bucket_name, object_name)
print(f"Successful image upload to bucket")

print("Generating presigned URL ...")
response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
)

print(f"Presigned URL generated successfully! This URL will expire in {expires_in} seconds (7 days):")
print(response)




