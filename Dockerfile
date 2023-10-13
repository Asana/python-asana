FROM python:3

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY asana /app/asana
COPY examples /app/examples
COPY tests /app/tests
COPY setup.py /app/setup.py
COPY README.md /app/README.md

RUN find . -name '*.pyc' -delete

RUN python --version
RUN python -m pytest

RUN python setup.py bdist_egg
