from gsheets import Sheets


def fetch_google_doc_content(doc_id: str) -> str:
    sheets = Sheets.from_files('client_secrets.json', 'storage.json')
    
    return sheets.get(doc_id).sheets[0].to_csv()
