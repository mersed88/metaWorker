FROM python:3.9-rc-slim

WORKDIR /home/app

COPY requirements.txt  requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY alembic alembic
COPY dto dto
COPY models models
COPY settings settings
COPY src src
COPY alembic.ini alembic.ini
COPY main.py main.py
COPY pr.py pr.py
COPY run_play.py run_play.py

CMD python main.py
