FROM python:3.10

COPY requirements.txt .
RUN pip install -r requirements.txt 

COPY ./prepare_data.py .
COPY ./train.py .