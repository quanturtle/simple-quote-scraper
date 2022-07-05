FROM python:3.8-slim-buster

RUN pip install --upgrade pip
RUN apt-get update -y

COPY . /app
WORKDIR /app

EXPOSE 420

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
