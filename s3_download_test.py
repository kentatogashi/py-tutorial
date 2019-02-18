import boto3

bucket_name = 'tktk012345-db1-s3'
object_name = 'ilb.png'
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)
bucket.download_file(object_name, object_name)
