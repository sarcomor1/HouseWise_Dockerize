FROM python:3.10-slim

WORKDIR /app

RUN apt update && apt install -y gcc libpq-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x wait-for-it.sh

CMD ["python", "app.py"]

