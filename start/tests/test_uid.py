import os
from datetime import datetime, timedelta,date,timezone
from email.utils import parseaddr

from dotenv import load_dotenv
from imap_tools import MailBox

load_dotenv()

HOST = os.environ.get("HOST")
EMAIL = os.environ.get("EMAIL")
PASSWORD  = os.environ.get("PASSWORD")
criteria="UID 4283"
with MailBox(HOST).login(EMAIL, PASSWORD) as box:
    for msg in box.fetch(criteria,charset='utf-8'):
        raw_from = msg.headers.get('from', [''])[0]
        from_name, from_email = parseaddr(raw_from)
        print(from_name, from_email)
