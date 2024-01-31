import lakefs
from lakefs.client import Client
import os
from dotenv import load_dotenv
import csv
from collections import deque

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


async def get_lakefs_logdata():    
    repo = lakefs.Repository("tpcoded", client=clt).branch("main")
    data = repo.object("log/morgan.txt") 
    return list(csv.reader((data.reader(mode='r'))))[-10:]   ## might get slower overtime as we read all lines, not optimal
   
