from pdfquery import PDFQuery
import fitz, pathlib , sys
import pandas as pd
import re

def get_pdf_data(file_path):
    pdf = PDFQuery(file_path)
    pdf.load()
    text_elements = pdf.pq('LTTextLineHorizontal') # type: ignore
    text = [t.text for t in text_elements]
    return text



def get_pdf_data2(file_path):
    docs = fitz.open(file_path) # type: ignore
    returndata = []
    page = docs[1]
    words = page.get_text("words")     
    with docs as doc: # type: ignore
        text = chr(12).join([page.get_text() for page in doc])        
    textlist = text.split(sep='\x0c')
    textlist = [t.split('\n') for t in textlist]
    removelist = ['SE MERE PÅ SIDE','GÆLDER FRA LØRDAG DEN', 'Spotvarer fås kun så længe lager haves. Nogle butikker fører ikke spotvarer og nonfoodvarer']
    textlist = [[t for t in lst if not any(r in t for r in removelist)] for lst in textlist]
    textlist = [lst for lst in textlist if lst] # remove empty lists
    page1 = ''
    for x in textlist[0]:        
        page1 += x +''    
    page1 = re.split(r"\.(?=-)", page1)
    page1 = [x for x in page1 if len(x) >= 5] # remove strings with less than 5 characters    
    return page1


