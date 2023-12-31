# Import the libraries
from dotenv import load_dotenv
import os
import sys
import pandas as pd
import boto3
from io import BytesIO


# Function to load CSV files from S3 bucket
def load_csv_file(bucket_name: str, file_key: str) -> pd.DataFrame:
    try:
        s3 = boto3.client("s3")  # Initialize boto3 client
        obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        df = pd.read_csv(BytesIO(obj["Body"].read()))
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        df = pd.DataFrame()  # Return an empty DataFrame in case of an error
    return df


# Function to load PARQUET file(s) from S3 bucket
def load_parquet_file(bucket_name: str, file_key: str) -> pd.DataFrame:
    try:
        s3 = boto3.client("s3")  # Initialize boto3 client
        obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        df = pd.read_parquet(BytesIO(obj["Body"].read()))
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        df = pd.DataFrame()  # Return an empty DataFrame in case of an error
    return df
