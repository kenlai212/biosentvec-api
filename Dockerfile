# syntax=docker/dockerfile:1

FROM python:3.9

WORKDIR /python-docker

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD python3 -m nltk.downloader stopwords;python3 -m nltk.downloader punkt;python3 -m flask run --host=0.0.0.0