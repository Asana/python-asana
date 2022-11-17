FROM python:3

WORKDIR /app

ADD requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ADD asana /app/asana
ADD examples /app/examples
ADD tests /app/tests
ADD setup.py /app/setup.py
ADD README.md /app/README.md

RUN find . -name '*.pyc' -delete

RUN python --version
RUN python -m pytest

RUN python setup.py bdist_egg
