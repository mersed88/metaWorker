# coding: utf-8
import io
import json
import pickle

import uvicorn
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import requests

from dto.profile import ProfileOut
from dto.worker import WorkerOut, WorkerIn
from settings.config import HOST, PORT, logger, url, headers
from src.init_db import init_db
from src.run_scenario import Scenario

sched = BackgroundScheduler(daemon=True)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get('/healthcheck')
async def HealthCheck():
    """Функция проверки что сервис работает"""
    return JSONResponse(status_code=200, content={})


@sched.scheduled_job('interval', seconds=10000000)
def job():
    try:
        profile: ProfileOut = ProfileOut(**requests.get(url=f"{url}/GetProfile", headers=headers, data=json.dumps({})).json())
        # task = requests.get(url=f"{url}/GetTask", headers=headers, data=json.dumps({})).json()
        # task = io.BytesIO(task.content)
        # pick = pickle.loads(task.getbuffer())
        # pick()
        for cookie in json.loads(profile.deviceCookies.device_cookies):
            play.add_cookie(cookie=cookie)

        play.run("yandex.ru")

        # TODO выполнение задачи
    except Exception as e:
        logger.error(e)


play = Scenario()
if __name__ == '__main__':
    profile: ProfileOut = ProfileOut(
        **requests.get(url=f"{url}/GetProfile", headers=headers, data=json.dumps({})).json())
    # task = requests.get(url=f"{url}/GetTask", headers=headers, data=json.dumps({})).json()
    # task = io.BytesIO(task.content)
    # pick = pickle.loads(task.getbuffer())
    # pick()
    for cookie in json.loads(profile.deviceCookies.device_cookies):
        play.add_cookie(cookie=cookie)

    play.run("yandex.ru")
