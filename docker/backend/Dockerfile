FROM python:3.9

WORKDIR /code

RUN apt update -qy && apt -qy upgrade

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
