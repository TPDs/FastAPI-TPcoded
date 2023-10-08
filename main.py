from fastapi import FastAPI
from dotenv import load_dotenv
from util.pocketbase import pb_db
import json

load_dotenv() 

app = FastAPI()
pb = pb_db().get_db()


@app.get("/")
async def root():
    with open('testdata.json') as f:
        data = json.load(f)
    result =  pb.collection('project').get_full_list()
    print(data)
    
    return result