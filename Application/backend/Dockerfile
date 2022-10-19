FROM python:3.9

WORKDIR /usr/src/app

RUN apt-get update && apt-get upgrade -y

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

ENV URL_PARAM=api
ENV DISPLAY_NAME=API

ENV NGINX_SERVER=http://localhost:8000
#ENV NGINX_SERVER=http://nginx:8000

ENV UVICORN_HOST=0.0.0.0
ENV UVICORN_PORT=8000
ENV UVICORN_WORKERS=2

COPY . .

CMD ["gunicorn", "-c", "gunicorn.conf.py", "app.main:app"]