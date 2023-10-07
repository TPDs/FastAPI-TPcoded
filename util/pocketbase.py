from pocketbase import PocketBase  # Client also works the same
from pocketbase.client import FileUpload
import os
from dotenv import load_dotenv

load_dotenv()

PUBLIC_PB_URL = os.getenv('PUBLIC_PB_URL')
PUBLIC_PB_ADMIN = os.getenv('PUBLIC_PB_ADMIN')
PUBLIC_PB_PW = os.getenv('PUBLIC_PB_PW')

client = PocketBase(PUBLIC_PB_URL)
admin_data = client.admins.auth_with_password(PUBLIC_PB_ADMIN, PUBLIC_PB_PW)

