FROM python:3.11

WORKDIR /data

COPY requirements.txt /data/

RUN pip install -r requirements.txt

COPY . /data/

EXPOSE 8000

CMD python flask1.py 0.0.0.0:4200