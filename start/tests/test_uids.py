import os
from email.utils import parseaddr

from dotenv import load_dotenv
from start.imap_tools import MailBox

load_dotenv()

HOST = os.environ.get("HOST")
EMAIL = os.environ.get("EMAIL")
PASSWORD  = os.environ.get("PASSWORD")
criteria="UID 4293:*"
with MailBox(HOST).login(EMAIL, PASSWORD) as box:
    for msg in box.fetch(criteria,charset='utf-8'):
        print(msg.date)