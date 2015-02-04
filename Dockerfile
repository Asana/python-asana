FROM ubuntu:14.04

RUN apt-get update

RUN apt-get install -y python python-pip
RUN apt-get install -y python3 python3-pip

WORKDIR /app

ADD requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
RUN pip3 install -r requirements.txt

ADD asana /app/asana
ADD tests /app/tests
ADD setup.py /app/setup.py

RUN find . -name '*.pyc' -delete

RUN python --version
RUN python -m pytest

RUN python3 --version
RUN python3 -m pytest

RUN python setup.py bdist_egg
RUN python3 setup.py bdist_egg
