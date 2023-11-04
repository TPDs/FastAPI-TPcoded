from pdfquery import PDFQuery
import fitz
import pandas as pd

def get_pdf_data(file_path):
    pdf = PDFQuery(file_path)
    pdf.load()
    text_elements = pdf.pq('LTTextLineHorizontal')
    text = [t.text for t in text_elements]
    return text


def get_pdf_data2(file_path):
    doc = fitz.open(file_path)
    page1 = doc[0]
    words = page1.get_text("words")

    return words
