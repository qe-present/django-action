from datetime import datetime, timedelta,date,timezone
from zoneinfo import ZoneInfo
import regex

from imap_tools import AND, MailBox,OR
import os
from dotenv import load_dotenv
load_dotenv()

HOST = os.environ.get("HOST")
EMAIL = os.environ.get("EMAIL")
PASSWORD  = os.environ.get("PASSWORD")
today = date.today()
c1=AND(date_gte=today, date_lt=today + timedelta(days=1))
c1=str(c1)
pattern = regex.compile(r'(?<content>(?<rec>\((?:[^()]++|(?&rec))*\)))')

for m in pattern.finditer(c1):
    c1=m.group('content')[1:-1]
with MailBox(HOST).login(EMAIL, PASSWORD) as box:
    for msg in box.fetch(criteria=c1,charset='utf-8'):
        print(msg.uid, msg.subject, msg.date_str)
