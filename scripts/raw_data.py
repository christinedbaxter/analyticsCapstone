# Import the libraries
from dotenv import load_dotenv
from io import StringIO
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

scripts_path = os.getenv("SCRIPTS_PATH")

# Add the path to the scripts folder to the sys.path list
if scripts_path is not None:
    if scripts_path not in sys.path:
        sys.path.append(scripts_path)

from get_data import load_csv_file, load_parquet_file

def get_raw_dataframes():
    # Define the bucket name and file keys
    bucket_name = "migraine-pressure-6week-analysis"
    url_cities = "weather/cities.csv"
    url_countries = "weather/countries.csv"
    url_daily_weather = "weather/daily_weather.parquet"
    url_migraine_1 = "health/IHME-GBD_2019_DATA-2c1d3941/IHME-GBD_2019_DATA-2c1d3941-1.csv"
    url_migraine_2 = "health/IHME-GBD_2019_DATA-2c1d3941/IHME-GBD_2019_DATA-2c1d3941-2.csv"
    url_migraine_3 = "health/IHME-GBD_2019_DATA-2c1d3941/IHME-GBD_2019_DATA-2c1d3941-3.csv"
    file_keys = [url_migraine_1, url_migraine_2, url_migraine_3]
    # url_migraine = "health/IHME-GBD_2019_DATA-eb4a1b02-1.csv"    
    # url_migraine = "health/IHME-GBD_2019_DATA-361f72c5-1.csv"

    # Load the data into dataframes
    df_cities = load_csv_file(bucket_name, url_cities)
    df_countries = load_csv_file(bucket_name, url_countries)
    df_daily_weather = load_parquet_file(bucket_name, url_daily_weather)

    # Load the migraine data into a single dataframe
    data_frames = []
    for file_key in file_keys:
        df = load_csv_file(bucket_name, file_key)
        data_frames.append(df)
    df_migraine = pd.concat(data_frames)

    return df_cities, df_countries, df_daily_weather, df_migraine
