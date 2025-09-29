# Django项目 - IFLOW.md

## 项目概述

这是一个基于Django 5.2.6的Web应用项目，使用SQLite数据库和ASGI服务器配置。项目结构为标准Django应用布局，包含主要的Django配置文件和一个api应用模块。

### 主要技术栈
- **框架**: Django 5.2.6
- **数据库**: SQLite3
- **服务器**: ASGI (支持Uvicorn)
- **Python版本**: 3.13+ (基于__pycache__中的编译文件)

## 项目结构

```
F:\code\Python\django-action\start\
├───api/                    # Django应用模块
│   ├───migrations/         # 数据库迁移文件
│   ├───__init__.py
│   ├───admin.py           # 后台管理配置
│   ├───apps.py            # 应用配置
│   ├───models.py          # 数据模型定义
│   ├───tests.py           # 测试文件
│   └───views.py           # 视图函数
├───start/                  # 主项目配置目录
│   ├───__pycache__/       # Python编译缓存
│   ├───__init__.py
│   ├───asgi.py            # ASGI配置
│   ├───settings.py        # Django设置
│   ├───urls.py            # URL路由配置
│   └───wsgi.py            # WSGI配置
├───static/                 # 静态文件目录
├───db.sqlite3             # SQLite数据库文件
├───manage.py              # Django管理脚本
└───README.md              # 项目文档
```

## 运行和开发

### 启动开发服务器

项目支持两种启动方式：

1. **使用Uvicorn ASGI服务器** (推荐方式):
```bash
uvicorn start.asgi:application --reload --host 127.0.0.1 --port 8000
```

2. **使用Django内置开发服务器**:
```bash
python manage.py runserver
```

### 数据库操作

```bash
# 创建数据库迁移
python manage.py makemigrations

# 应用数据库迁移
python manage.py migrate

# 创建超级用户
python manage.py createsuperuser
```

### 静态文件管理

```bash
# 收集静态文件
python manage.py collectstatic
```

## 配置详情

### 数据库配置
- **引擎**: Django SQLite3
- **数据库文件**: `db.sqlite3` (位于项目根目录)
- **配置位置**: `start/settings.py:78-83`

### 静态文件配置
- **静态URL**: `/static/`
- **静态根目录**: `static/` (位于项目根目录)
- **配置位置**: `start/settings.py:125-130`

### 应用配置
- **已安装应用**: 仅包含Django内置应用，api应用尚未添加到INSTALLED_APPS
- **中间件**: 标准Django安全中间件配置
- **模板配置**: 使用Django模板引擎，默认配置

## 开发状态

### 当前状态
- ✅ Django项目基础结构已搭建
- ✅ 数据库配置完成
- ✅ ASGI/WSGI配置完成
- ✅ 静态文件配置完成
- ⚠️ api应用已创建但未注册到INSTALLED_APPS
- ⚠️ 数据模型、视图、URL路由尚未开发
- ⚠️ 项目功能待实现

### 下一步开发建议

1. **注册api应用**: 在`start/settings.py`的INSTALLED_APPS中添加`'api'`
2. **定义数据模型**: 在`api/models.py`中定义业务数据模型
3. **创建视图**: 在`api/views.py`中实现业务逻辑视图
4. **配置URL路由**: 在`start/urls.py`和`api/urls.py`中配置URL路由
5. **创建模板**: 如需前端页面，创建相应的HTML模板
6. **编写测试**: 在`api/tests.py`中编写单元测试

## 安全注意事项

- **DEBUG模式**: 当前DEBUG=True，仅适用于开发环境
- **SECRET_KEY**: 使用默认生成的密钥，生产环境需要更换
- **ALLOWED_HOSTS**: 当前为空列表，生产环境需要配置允许的域名

## 开发约定

- 遵循Django官方开发最佳实践
- 使用Python 3.13+语法特性
- 数据库迁移需要严格执行makemigrations和migrate流程
- 静态文件通过collectstatic命令统一管理