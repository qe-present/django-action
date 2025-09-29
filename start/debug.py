#!/usr/bin/env python
import os, sys, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'start.settings')
django.setup()
from django.core.management import execute_from_command_line
execute_from_command_line(['manage.py', 'makemigrations', 'api'])