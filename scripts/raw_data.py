# Import the libraries
from dotenv import load_dotenv
import os
import sys
import pandas as pd
import boto3

load_dotenv("../config/.env")

# Initialize S3 client with environment variables
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

# Add the path to the scripts folder and import the functions
sys.path.append("../scripts/")
from get_data import load_csv_file, load_parquet_file


def get_raw_dataframes():
    # Define the bucket name and file keys
    bucket_name = "migraine-pressure-6week-analysis"
    url_cities = "weather/cities.csv"
    url_countries = "weather/countries.csv"
    url_daily_weather = "weather/daily_weather.parquet"
    url_migraine = "health/IHME-GBD_2019_DATA-361f72c5-1.csv"

    # Load the data into dataframes
    df_cities = load_csv_file(bucket_name, url_cities)
    df_countries = load_csv_file(bucket_name, url_countries)
    df_daily_weather = load_parquet_file(bucket_name, url_daily_weather)
    df_migraine = load_csv_file(bucket_name, url_migraine)

    return df_cities, df_countries, df_daily_weather, df_migraine
