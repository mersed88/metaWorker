# coding: utf-8
import json

import uvicorn
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import requests

from dto.worker import WorkerOut, WorkerIn
from settings.config import host, port, logger, url, headers
from src.init_db import init_db

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


@sched.scheduled_job('interval', seconds=10)
def job():
    try:
        param = WorkerIn(id=1)
        task = WorkerOut(**requests.get(url=url, headers=headers, data=json.dumps(param)).json())
        # TODO выполнение задачи
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    uvicorn.run(app, host=str(host), port=int(port), debug=False)
