from email.utils import parsedate_to_datetime
from datetime import timezone
from zoneinfo import ZoneInfo

s = 'Tue, 30 Sep 2025 05:35:17 -0500 (CDT)'
dt_raw = parsedate_to_datetime(s)          # 保留原始 -05:00
dt_sh = dt_raw.astimezone(ZoneInfo("Asia/Shanghai"))

print("上海时区:", dt_sh)         # 2025-09-30 18:35:17+08:00
