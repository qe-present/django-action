import asyncio
from datetime import date, timedelta
from typing import Optional, List, Iterable, AsyncGenerator
from imap_tools import MailBox, AND
import regex
class EmailManager:
    def __init__(self, host: str, email: str, password: str, folder: str = "INBOX"):
        self.host = host
        self.email = email
        self.password = password
        self.folder = folder

    def _connect(self):
        return MailBox(self.host).login(self.email, self.password, initial_folder=self.folder)

    def get_meail_by_uid(self,uid:int):
        """根据UID获取邮件"""
        with self._connect() as m:
            for msg in m.fetch(AND(uid=uid)):
                return msg
        return None
    def iter_emails_in_period(self, limit: Optional[int] = None) -> Iterable:
        """迭代最近 days 天内的邮件（含今天），可指定 limit、是否反向、是否只取头部。"""
        end_date = date.today() + timedelta(days=1)      # BEFORE 为不含 -> 用明天
        start_date = end_date - timedelta(days=limit)     # 含 start_date
        criteria = AND(date_gte=start_date, date_lt=end_date)
        c1 = str(criteria)
        pattern = regex.compile(r'(?<content>(?<rec>\((?:[^()]++|(?&rec))*\)))')
        for m in pattern.finditer(c1):
            criteria = m.group('content')[1:-1]
        with self._connect() as m:
            for msg in m.fetch(criteria):
                yield msg

    def get_last_month_emails(self, limit: Optional[int] = None) -> List:
        """获取最近的邮件列表，可选 limit。"""
        return list(self.iter_emails_in_period(limit=limit))

    def print_last_month_summary(self, limit: Optional[int] = None):
        msgs = self.get_last_month_emails(limit=limit)
        if not msgs:
            print(f"最近{limit}天无邮件")
            return
        else:
            return msgs


class AsyncEmailManager:
    def __init__(self, sync_manager: EmailManager):
        self.sync = sync_manager

    async def get_last_email_fast(self):
        return await asyncio.to_thread(self.sync.get_last_email_fast)

    async def get_last_email_by_uid(self):
        return await asyncio.to_thread(self.sync.get_last_email_by_uid)

    async def iter_emails_in_period(self, days: int = 30, limit: Optional[int] = None,
                                    reverse: bool = False, headers_only: bool = False) -> AsyncGenerator:
        def collect():
            return list(self.sync.iter_emails_in_period(limit=limit))
        msgs = await asyncio.to_thread(collect)
        for m in msgs:
            yield m

    async def get_last_month_emails(self, limit: Optional[int] = None) -> List:
        def collect():
            return self.sync.get_last_month_emails(limit=limit)
        return await asyncio.to_thread(collect)

    async def print_last_month_summary(self, limit_date: Optional[int] = None):
        msgs = await self.get_last_month_emails(limit=limit_date)
        if not msgs:
            return "没有同步成功"
        else:
            return msgs

    async def get_email_by_uid(self, uid: int):
        return await asyncio.to_thread(self.sync.get_meail_by_uid, uid)



