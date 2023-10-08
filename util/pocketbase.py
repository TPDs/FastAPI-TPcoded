from pocketbase import PocketBase  # Client also works the same
from pocketbase.client import FileUpload
import os
from dotenv import load_dotenv

load_dotenv()

PUBLIC_PB_URL = os.getenv('PUBLIC_PB_URL')
PUBLIC_PB_ADMIN = os.getenv('PUBLIC_PB_ADMIN')
PUBLIC_PB_PW = os.getenv('PUBLIC_PB_PW')

client = PocketBase(PUBLIC_PB_URL)

class pb_db:
    __instance__ = None

    def __int__(self):
        if pb_db.__instance__ is None:
            pb_db.__instance__ = client.admins.auth_with_password(PUBLIC_PB_ADMIN, PUBLIC_PB_PW)
        else:
            raise Exception("DB Conn findes allerede")

    @staticmethod
    def get_db():
        if not pb_db.__instance__:
            pb_db.__instance__ = client.admins.auth_with_password(PUBLIC_PB_ADMIN, PUBLIC_PB_PW)
        return client
