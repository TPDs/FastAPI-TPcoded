from fastapi import FastAPI
from pathlib import Path
from dotenv import load_dotenv
import uvicorn
from util.pocketbase import pb_db
from util.google_docs import load_service_account_credentials
from googleapiclient.discovery import build
import httpx
import os

scopes = ['https://www.googleapis.com/auth/documents.readonly',
          'https://www.googleapis.com/auth/drive.file']
gauth = load_service_account_credentials(
    'tpcoded-docreader.json', scopes)


load_dotenv() 
host = os.getenv('HOST')
app = FastAPI()
pb = pb_db().get_db()
demodoc = "1DTNmbe4NNJcBQtolMO5r2fvNRzXaCnPnKoYAeTHugdE"

@app.get("/test")
async def root():
    result = pb.collection('project').get_full_list() 
    return result


@app.get("/")
async def get_doc_content():  
    docs_service = build('docs', 'v1', credentials=gauth)
    drive_service = build('drive', 'v3', credentials=gauth)
    return build('docs', 'v1', credentials=gauth).documents().get(documentId=demodoc).execute().get('body').get('content')


@app.get("/create")
async def create_doc_content():      
    return "test"



if __name__ == '__main__':
    uvicorn.run(f"{Path(__file__).stem}:app", port=5273, host=host, reload=True) # type: ignore