#!/bin/bash
# upload_presign.sh

# Positional arguments
LOCAL_FILE=$1         
BUCKET_NAME=$2        
EXPIRES_IN=604800     


if [ -z "$LOCAL_FILE" ] || [ -z "$BUCKET_NAME" ]; then
  echo "Usage: $0 LOCAL_FILE BUCKET_NAME"
  exit 1
fi


echo "Uploading $LOCAL_FILE to s3://$BUCKET_NAME/"
aws s3 cp "$LOCAL_FILE" "s3://$BUCKET_NAME/"

if [ $? -ne 0 ]; then
  echo "Upload failed."
  exit 1
fi


URL=$(aws s3 presign "s3://$BUCKET_NAME/$LOCAL_FILE" --expires-in "$EXPIRES_IN")

if [ $? -ne 0 ]; then
  echo "Failed to generate presigned URL."
  exit 1
fi

echo "Presigned URL (valid for 7 days):"
echo "$URL"
