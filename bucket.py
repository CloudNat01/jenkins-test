# import boto3
# #from boto3 import Session
# session = boto3.Session(profile_name="default")

# s3 = boto3.client("s3")
# s3.create_bucket(Bucket="loveth-oballe-buck-xl")
                                           
import boto3

sess= boto3.Session(region_name='us-east-2')
s3client = sess.client('s3')
bucket_name='loveth-likes-to-try'
s3_location={
    'LocationConstraint': 'us-east-2'
}
s3client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)
