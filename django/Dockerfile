FROM python:3.11

WORKDIR /data

COPY requirements.txt /data/

RUN pip install -r requirements.txt

RUN pip install psycopg2-binary --force-reinstall --no-cache-dir

COPY . /data/

EXPOSE 8000