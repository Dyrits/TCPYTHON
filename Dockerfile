FROM python:3.12-slim

RUN apt-get update && apt-get install -y nmap

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4500

CMD ["python", "scanner.py"]