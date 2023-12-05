from fastapi import FastAPI
from pathlib import Path
from dotenv import load_dotenv
import uvicorn
from util.pocketbase import pb_db
import os


load_dotenv() 
host = os.getenv('HOST')
app = FastAPI()
pb = pb_db().get_db()


@app.get("/test")
async def root():
    result = pb.collection('project').get_full_list() 
    return result


@app.get("/")
async def get_doc_content():   
    
    return "content"


@app.get("/create")
async def create_doc_content():      
    return "test"



if __name__ == '__main__':
    uvicorn.run(f"{Path(__file__).stem}:app", port=5273, host=host, reload=True) # type: ignore