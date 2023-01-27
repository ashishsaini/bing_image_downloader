FROM --platform=linux/amd64 python:3.8-slim-buster

RUN  apt-get update \ 
    && apt-get install -y build-essential python3-dev

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "main.py"]