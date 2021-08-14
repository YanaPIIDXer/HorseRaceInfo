FROM python:3.8

ENV PYTHONBUFFERED 1
WORKDIR /app

ADD ./requirements.txt /app
RUN pip install -r requirements.txt

ADD ./src /app

EXPOSE 80
CMD ["python", "manage.py", "runserver", "0:80"]
