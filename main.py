# coding: utf-8
import io
import json
import pickle
import ast
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
from run_play import Scenario as play

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
    init_db()
    sched.start()


@app.get('/healthcheck')
async def HealthCheck():
    """Функция проверки что сервис работает"""
    return JSONResponse(status_code=200, content={})


@sched.scheduled_job('interval', seconds=10)
def job():
    try:
        profile: ProfileOut = ProfileOut(**requests.get(url=f"{url}/GetProfile", headers=headers, data=json.dumps({})).json())
        task = requests.get(url=f"{url}/GetTask", headers=headers, data=json.dumps({}))
        tt = 0
        if task.status_code == 200:
            logger.info("start scenario")
            game = play()
            for item in ast.literal_eval(profile.deviceCookies.device_cookies.decode()):
                try:
                    game.add_cookie(
                        item
                    )
                    tt+=1
                except Exception as e:
                    print(tt)
            game.start()
        #task = io.BytesIO(task.content)
        # with open ("test_data.pkl","wb") as file:
        #     file.write(task.getbuffer())

        # with open ("scenario.pkl","rb") as file:
        #     pick = pickle.load(file)
        # pick.start()

        # for cookie in json.loads(profile.deviceCookies.device_cookies):
        #     play.add_cookie(cookie=cookie)
        #
        # play.run("yandex.ru")

        # TODO выполнение задачи
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    ...

    # with open("scenario.pkl", "rb") as file:
    #     pick = pickle.load(file)
    # a = pick
    # a.start()
    uvicorn.run(app=app, host=HOST,port=PORT)
    # profile: ProfileOut = ProfileOut(
    #     **requests.get(url=f"{url}/GetProfile", headers=headers, data=json.dumps({})).json())
    # # task = requests.get(url=f"{url}/GetTask", headers=headers, data=json.dumps({})).json()
    # # task = io.BytesIO(task.content)
    # # pick = pickle.loads(task.getbuffer())
    # # pick()
    # for cookie in json.loads(profile.deviceCookies.device_cookies):
    #     play.add_cookie(cookie=cookie)
    #
    # play.run("yandex.ru")
