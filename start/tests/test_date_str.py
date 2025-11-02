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
c1="SMALLER  8511"
print(c1)
with MailBox(HOST).login(EMAIL, PASSWORD) as box:
    for msg in box.uids(criteria=c1,charset='utf-8'):
        print(msg)
