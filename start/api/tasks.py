from typing import List

from celery import shared_task
from imap_tools.message import MailMessage
from .email import EmailAddSerializer
from utils import get_email_by_days,message_to_dict
import asyncio

@shared_task(bind=True)
def send_email_task(self,uid:int=0,days: int = 1) -> str:
    messages:List[MailMessage]=asyncio.run(get_email_by_days(days))
    data_list = [message_to_dict(m) for m in messages]
    serializer = EmailAddSerializer(data=data_list, many=True)
    if serializer.is_valid():
        serializer.save()
    else:
        print("数据序列化失败:", serializer.errors)
    return "同步邮箱成功"



