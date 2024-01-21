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

def get_client():
    return clt


def get_lakefs():
    repo = lakefs.Repository("tpcoded", client=clt).branch("main").object("log/morgan.log")
    print(repo)
    return repo
