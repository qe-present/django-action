from .email import EmailManager,AsyncEmailManager
from dotenv import load_dotenv
import os
load_dotenv()
HOST = os.environ.get("HOST")
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
def message_to_dict(msg):
    return {
        "uid": msg.uid,
        "to": msg.to[0],
        "from_email": msg.from_,
        "subject": msg.subject,
        "cc": msg.cc or [],
        "bcc": msg.bcc or [],
        "date": msg.date,
        "text": msg.text or "",
        "html": msg.html or "",
        "attachments": msg.attachments or [],
        "size": msg.size or 0,
    }


async def get_email_by_days(limit_date:int):
    """
    获取limit_date天的邮件
    :param limit_date:
    :return:
    """
    sync_mgr = EmailManager(HOST, EMAIL, PASSWORD)
    async_mgr = AsyncEmailManager(sync_mgr)
    return await async_mgr.print_last_month_summary(limit_date=limit_date)
async def get_one_email(uid:int):
    """
    获取最新一封邮件
    :return:
    """
    sync_mgr = EmailManager(HOST, EMAIL, PASSWORD)
    async_mgr = AsyncEmailManager(sync_mgr)
    return await async_mgr.get_email_by_uid(uid)
