import boto3
from boto3 import Session
session = boto3.Session(profile_name="admin", region_name="us-east-1")

s3 = boto3.client("s3")
s3.create_bucket(Bucket="loveth-oballe-buck-xl")
                                           
