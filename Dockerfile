FROM python:3.10

COPY requirements.txt .
RUN pip install -r requirements.txt 

COPY ./src/prepare_data.py .
COPY ./src/train.py .