# Description: This script contains functions to load data from S3 bucket

# Import libraries
import pandas as pd
import boto3
from io import BytesIO

# Function to load CSV files from S3 bucket
def load_csv_file(bucket_name, file_key):
    try:        
        s3 = boto3.client('s3')    # Initialize boto3 client
        obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        df = pd.read_csv(BytesIO(obj['Body'].read()))
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
# Function to load PARQUET file(s) from S3 bucket
def load_parquet_file(bucket_name, file_key):
    try:
        s3 = boto3.client('s3')    # Initialize boto3 client
        obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        df = pd.read_parquet(BytesIO(obj['Body'].read()))        
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    