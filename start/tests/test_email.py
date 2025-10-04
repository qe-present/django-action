#!/usr/bin/env python3
# 只用标准库，不装 imap_tools
import imaplib
import email
from datetime import datetime, timezone, date, timedelta
from email.utils import parsedate_to_datetime, parseaddr

# ---------- 配置 ----------
import os
from zoneinfo import ZoneInfo

from dotenv import load_dotenv
load_dotenv()

HOST = os.environ.get("HOST")
EMAIL = os.environ.get("EMAIL")
PASSWORD  = os.environ.get("PASSWORD")
SSL       = True   # 993；如果想 143 就 False
# --------------------------

today_start = datetime.combine(date.today(), datetime.min.time()).replace(tzinfo=timezone.utc)
tomorrow_start = today_start + timedelta(days=1)

def open_connection():
    """返回已登录的 IMAP4 对象"""
    cls = imaplib.IMAP4_SSL if SSL else imaplib.IMAP4
    conn = cls(HOST)
    conn.login(EMAIL, PASSWORD)
    conn.select('INBOX')          # 只读方式打开 INBOX
    return conn

def fetch_today_by_date_header(conn):
    """
    先让服务器粗筛最近 7 天，再按 Date 头精确过滤今天
    """
    since_str = (date.today()).strftime('%d-%b-%Y')
    print(since_str)
    typ, data = conn.search(None, f'SINCE {since_str}')   # data=[b'uid1 uid2 ...']
    if typ != 'OK':
        return
    uid_list = data[0].split()
    print(uid_list)
    for uid in uid_list:
        # 一次性拉下整个 RFC822 文本
        typ, msg_data = conn.fetch(uid, '(RFC822)')
        print(11111)
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)
        date_header = msg.get('Date')
        print('Date header:', date_header)
        date_header = parsedate_to_datetime(date_header)
        dt_sh = date_header.astimezone(ZoneInfo("Asia/Shanghai"))
        print(dt_sh)


if __name__ == '__main__':
    conn = open_connection()
    try:
        fetch_today_by_date_header(conn)
    finally:
        conn.close()
        conn.logout()