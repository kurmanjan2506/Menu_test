FROM python

ENV PYTHONUNBUFFERED 1

WORKDIR /project

COPY requirements.txt /project/

RUN apt-get update -y && apt-get upgrade -y

RUN pip install -r requirements.txt

COPY . /project/