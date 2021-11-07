# _setup.py: Create clients, load data, etc. No need to edit.
import boto3, pandas as pd

# Load Data
data_url = "https://assets.datacamp.com/production/repositories/5668/datasets/6bba555e0e42ae31d1d634256679db718cfb8d76/vehicles.csv"
records = pd.read_csv(data_url).head(100)

# Create firehose client
firehose = boto3.client('firehose', 
    aws_access_key_id="None", 
    aws_secret_access_key="None", 
    region_name='us-east-1', 
    endpoint_url="http://localhost:4573")

# Create s3 client
s3 = boto3.client('s3', 
    aws_access_key_id="None", 
    aws_secret_access_key="None", 
    region_name='us-east-1', 
    endpoint_url="http://localhost:4572")
    
# Prep variables for export
ex_vars = [firehose, s3, records]
    
