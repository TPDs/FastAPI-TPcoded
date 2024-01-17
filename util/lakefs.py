import boto3
import lakefs
from lakefs.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv('LAKEFS_ID')
PASSWORD = os.getenv('LAKEFS_ACC')



clt = Client(
    host="http://192.168.1.25:8000",
    username=USER,
    password=PASSWORD,
)

clt.config.verify_ssl = False


def get_lakefs():
    print("Listing repositories:")
    for repo in lakefs.repositories(client=clt):
        print(repo)
    return 'test'
