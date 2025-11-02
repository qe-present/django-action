from datetime import timedelta,date
import regex

from start.imap_tools import AND, MailBox
import os
from dotenv import load_dotenv
load_dotenv()

HOST = os.environ.get("HOST")
EMAIL = os.environ.get("EMAIL")
PASSWORD  = os.environ.get("PASSWORD")
today = date.today()
c1=AND(date_gte=today, date_lt=today + timedelta(days=1))

with MailBox(HOST).login(EMAIL, PASSWORD) as box:
    for msg in box.fetch(criteria=c1,charset='utf-8'):
        print(msg.uid, msg.subject, msg.date_str)
