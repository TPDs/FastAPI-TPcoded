from fastapi import FastAPI
from pathlib import Path
from dotenv import load_dotenv
import uvicorn
from util.pocketbase import pb_db
from util.pdfparser import get_pdf_data2
import json
import os


load_dotenv() 
host = os.getenv('HOST')
app = FastAPI()
pb = pb_db().get_db()


@app.get("/")
async def root():
    with open('testdata.json') as f:
        data = json.load(f)
    result = pb.collection('project').get_full_list() 
    return data


@app.get("/pdf")
async def pdf():
    data = get_pdf_data2('netto.pdf')
    return data

if __name__ == '__main__':
    uvicorn.run(f"{Path(__file__).stem}:app", port=5273, host=host, reload=True) # type: ignore