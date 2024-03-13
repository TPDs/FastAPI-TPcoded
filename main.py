from fastapi import FastAPI
from pathlib import Path
from dotenv import load_dotenv
import uvicorn
import os
from util.pocketbase import pb_db
from util.lakefs import get_client, get_lakefs_logdata
from util.transformer import optimzer
from util.whois_parser import ip_parser

load_dotenv() 
host = os.getenv('HOST')
app = FastAPI()

Pocketbase = pb_db.get_db()
lake = get_client()


@app.get("/parse")
async def parser():
    return await get_lakefs_logdata()


@app.get("/data")
async def pb():
    result = Pocketbase.collection('project').get_full_list()    
    return result


@app.get("/")
async def lakefs():
    w = await get_lakefs_logdata()
    ww = await optimzer(w)
    www = await ip_parser(ww)   
    return www


if __name__ == '__main__':
    uvicorn.run(f"{Path(__file__).stem}:app", port=5273, host=host, reload=True) # type: ignore