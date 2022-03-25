FROM python:3.10-buster    

RUN mkdir /app

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt 

ENV FLASK_APP my_api

CMD flask run --host=0.0.0.0