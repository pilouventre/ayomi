FROM python:3.9.0

ADD requirements.txt /mysite/requirements.txt

WORKDIR /mysite

RUN pip install -r requirements.txt
ENV PYTHONPATH /mysite