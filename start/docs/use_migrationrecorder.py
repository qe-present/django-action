# 在 MigrationRecorder 类 的 内 部 定 义 了 一 个 模 型 类 ，
# 映 射 的 表 名 为 django_migrations。在刜始化方法中必须传入对应数据库的连接信息
"""
cd ../
python -m docs.use_migrationrecorder
带 -m 走“包导入”，项目根自动进 sys.path，相对导入不翻车；
直接 python file.py 走“脚本导入”，只加 file 所在目录，上层包就找不到。
"""
import os
import django

from django.db.migrations.recorder import MigrationRecorder
from django.db import connections

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "start.settings")
django.setup()
# 获取连接
connection = connections['default']
# 创建 MigrationRecorder 实例
recorder = MigrationRecorder(connection)
# 获取所有已应用的迁移记录
applied_migrations = recorder.applied_migrations()
# 打印已应用的迁移记录
for app, name in applied_migrations:
    print(f"App: {app}, Migration: {name}")
# 添加迁移记录
recorder.record_applied('start.api', 'test_migration')
# 删除迁移记录
recorder.record_unapplied('start.api', 'test_migration')
