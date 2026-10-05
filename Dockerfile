FROM python:3.9-slim

WORKDIR /app

COPY authenticator.py .

CMD ["python", "authenticator.py"]