from google.oauth2 import service_account
from googleapiclient.discovery import build
service_account_file = 'tpcoded-docreader.json'


def load_service_account_credentials(service_account_file, scopes):
    credentials = service_account.Credentials.from_service_account_file(
        service_account_file, scopes=scopes
    )
    return credentials






