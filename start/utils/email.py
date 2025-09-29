import asyncio
from datetime import date, timedelta
from typing import Optional, List, Iterable, AsyncGenerator

from imap_tools import MailBox, AND
EMAIL = "2664481691@qq.com"
PASSWORD = "wnxaqnkpflquecag"
IMAP_HOST="imap.qq.com"

class EmailManager:
    def __init__(self, host: str, email: str, password: str, folder: str = "INBOX"):
        self.host = host
        self.email = email
        self.password = password
        self.folder = folder

    def _connect(self):
        return MailBox(self.host).login(self.email, self.password, initial_folder=self.folder)

    def get_last_email_fast(self):
        """方式1: reverse=True + limit=1 直接拿最新一封"""
        with self._connect() as m:
            for msg in m.fetch(AND(all=True), reverse=True, limit=1):
                return msg
        return None

    def get_last_email_by_uid(self):
        """方式2: 根据最大 UID 精确获取"""
        with self._connect() as m:
            all_uids = m.uids(AND(all=True))
            if not all_uids:
                return None
            last_uid = all_uids[-1]  # 已按服务器顺序
            for msg in m.fetch(AND(uid=last_uid)):
                return msg
        return None
    def iter_emails_in_period(self, days: int = 30, limit: Optional[int] = None,
                              reverse: bool = False, headers_only: bool = False) -> Iterable:
        """迭代最近 days 天内的邮件（含今天），可指定 limit、是否反向、是否只取头部。"""
        end_date = date.today() + timedelta(days=1)      # BEFORE 为不含 -> 用明天
        start_date = end_date - timedelta(days=days)     # 含 start_date
        criteria = AND(date_gte=start_date, date_lt=end_date)
        with self._connect() as m:
            for msg in m.fetch(criteria, reverse=reverse, limit=limit, headers_only=headers_only):
                yield msg

    def get_last_month_emails(self, limit: Optional[int] = None) -> List:
        """获取最近30天邮件列表，可选 limit。"""
        return list(self.iter_emails_in_period(days=30, limit=limit, reverse=False))

    def print_last_month_summary(self, limit: Optional[int] = None):
        msgs = self.get_last_month_emails(limit=limit)
        if not msgs:
            print("最近30天无邮件")
            return
        for i, msg in enumerate(msgs, 1):
            print(
                f"{i}. UID={msg.uid} 日期={msg.date.strftime('%Y-%m-%d %H:%M')} 发件人={msg.from_} 主题={msg.subject}")

    def print_last_email(self):
        msg = self.get_last_email_fast()
        if not msg:
            print("没有邮件")
            return
        print("主题:", msg.subject)
        print("发件人:", msg.from_)
        print("日期:", msg.date_str)
        print("正文:", msg.html or msg.text)


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
            return list(self.sync.iter_emails_in_period(days=days, limit=limit,
                                                        reverse=reverse, headers_only=headers_only))
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
            print("最近30天无邮件")
            return
        for i, msg in enumerate(msgs, 1):
            print(f"{i}. UID={msg.uid} 日期={msg.date.strftime('%Y-%m-%d %H:%M')} 发件人={msg.from_} 主题={msg.subject}")

    async def print_last_email(self):
        msg = await self.get_last_email_fast()
        if not msg:
            print("没有邮件")
            return
        print("主题:", msg.subject)
        print("发件人:", msg.from_)
        print("日期:", msg.date_str)
        print("正文(截断):", (msg.text or msg.html or "").strip()[:200])

# 示例运行
async def main():
    sync_mgr = EmailManager(IMAP_HOST, EMAIL, PASSWORD)
    async_mgr = AsyncEmailManager(sync_mgr)
    await async_mgr.print_last_email()
    await async_mgr.print_last_month_summary(limit_date=30)

if __name__ == "__main__":
    asyncio.run(main())
