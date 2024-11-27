FROM python:3.12-alpine
LABEL maintainer="devlemosjose@gmail.com"

COPY application /application
COPY deploy /deploy

WORKDIR /application

EXPOSE 8000

RUN apk update && apk add --no-cache \
    netcat-openbsd \
    postgresql-dev \
    gcc \
    musl-dev \
    libffi-dev \
    postgresql \
    build-base 


RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip setuptools wheel && \
  /venv/bin/pip install --no-cache-dir -r /application/requirements.txt && \
  adduser --disabled-password --no-create-home duser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R duser:duser /venv && \
  chown -R duser:duser /data/web/static && \
  chown -R duser:duser /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /deploy


ENV PATH="/deploy:/venv/bin:$PATH"

USER duser

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

CMD ["commands.sh"]
