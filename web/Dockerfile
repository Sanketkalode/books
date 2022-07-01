FROM python:3.8-slim-buster
WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y netcat
RUN pip install --upgrade pip
COPY . /usr/src/app/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","run.py"]