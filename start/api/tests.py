from django.test import TestCase
from imap_tools import MailBox



EMAIL = "2664481691@qq.com"
PASSWORD = "wnxaqnkpflquecag"

with MailBox("imap.qq.com").login(EMAIL, PASSWORD, initial_folder="INBOX") as mailbox:
    for msg in mailbox.fetch(limit=5):
        print("主题：", msg.subject)
        print("发件人：", msg.from_)
        print("日期：", msg.date_str)
        print("正文：", msg.text or msg.html)
        print("-" * 40)