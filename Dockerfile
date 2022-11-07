FROM python:3.8-alpine

WORKDIR /home

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN apk add --update --no-cache --virtual .tmp-build-deps \
     gcc libc-dev linux-headers postgresql-dev tree vim

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "./manage.py", "runserver", "0.0.0.0:8001"]
