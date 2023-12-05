from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from fastapi import FastAPI
from pathlib import Path
from dotenv import load_dotenv
import uvicorn
from util.gsheet import fetch_google_doc_content
from util.pocketbase import pb_db
import os


load_dotenv() 
host = os.getenv('HOST')
demo_doc = os.getenv('DEMO_DOC') 
app = FastAPI()
pb = pb_db().get_db()


gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth)


@app.get("/test")
async def root():
    result = pb.collection('project').get_full_list() 
    return result


@app.get("/")
async def get_doc_content():    
    #content = drive.ListFile().GetList()
    return "content"


@app.get("/create")
async def create_doc_content():  
    drive.CreateFile({'title': 'Hello.txt', 'mimeType': 'text/plain'})
    return "test"



if __name__ == '__main__':
    uvicorn.run(f"{Path(__file__).stem}:app", port=5273, host=host, reload=True) # type: ignore