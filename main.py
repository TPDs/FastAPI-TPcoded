from fastapi import FastAPI
from pathlib import Path
from dotenv import load_dotenv
import uvicorn
import os
from util.pocketbase import pb_db
from util.lakefs import get_lakefs



load_dotenv() 
host = os.getenv('HOST')
app = FastAPI()

Pocketbase = pb_db.get_db()
lake = get_lakefs()


@app.get("/data")
async def pb():
    result = Pocketbase.collection('project').get_full_list()    
    return result


@app.get("/test")
async def lakefs():    
    
    return type(lake)


@app.get("/")
async def get_doc_content():  
    return "test2"


if __name__ == '__main__':
    uvicorn.run(f"{Path(__file__).stem}:app", port=5273, host=host, reload=True) # type: ignore