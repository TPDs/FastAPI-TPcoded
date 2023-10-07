from fastapi import FastAPI
from dotenv import load_dotenv
import os
from util import pocketbase as pb

load_dotenv() 

app = FastAPI()


@app.get("/")
async def root():

    result =  pb.client.collection('project').get_full_list()
    print(result)
    return result