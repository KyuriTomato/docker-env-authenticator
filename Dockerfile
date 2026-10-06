FROM python:3.11-slim

WORKDIR /app
# Wir erstellen den Datenordner im Container

RUN mkdir /data

COPY authenticator.py .

CMD ["python", "authenticator.py"]
