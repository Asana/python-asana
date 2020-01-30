FROM python:3

WORKDIR /usr/app

ADD requirements.txt /usr/app/requirements.txt

RUN pip install -r requirements.txt

ADD asana /usr/app/asana
ADD examples /usr/app/examples
ADD tests /usr/app/tests
ADD setup.py /usr/app/setup.py

RUN find . -name '*.pyc' -delete

RUN python --version

RUN python setup.py install
