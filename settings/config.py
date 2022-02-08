# coding: utf-8

import logging
import requests
import os
from cmreslogging.handlers import CMRESHandler
import yaml
import datetime

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(filename)s[LINE:%(lineno)d]# [%(asctime)s]-%(levelname)#-8s  %(message)s',
                    datefmt='%d-%m-%y %H:%M:%S',
                    level=logging.INFO)
logger.setLevel(logging.DEBUG)

headers = {'Content-Type': 'application/json;charset=UTF-8'}

HOST = str(os.getenv('HOST', '0.0.0.0'))
PORT = int(os.getenv('PORT', 8080))

user_postgres = os.getenv("USER_POSTGRES", "postgres")
password_postgres = os.getenv("PASSWORD_POSTGRES", "Nhjkm123")
host_postgres = os.getenv("HOST_POSTGRES", "188.120.237.127")
port_postgres = os.getenv("PORT_POSTGRES", "5432")
db_postgres = os.getenv("DB_POSTGRES", "postgres")

engine_string = f'postgresql+asyncpg://{user_postgres}:{password_postgres}@{host_postgres}:{port_postgres}/{db_postgres}'
schema_db = os.getenv("SCHEMA", "taskManager")

url = os.getenv("URL", "localhost:8080")
