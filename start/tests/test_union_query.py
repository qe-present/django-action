from datetime import datetime, timedelta

from start.imap_tools import MailBox, A
import os
from dotenv import load_dotenv
load_dotenv()

HOST = os.environ.get("HOST")
EMAIL = os.environ.get("EMAIL")
PASSWORD  = os.environ.get("PASSWORD")
criteria = 'SMALLER  8511'
with MailBox(HOST).login(EMAIL, PASSWORD) as box:
    for msg in box.client.uid("SEARCH", criteria)[1]:
        print(msg)
