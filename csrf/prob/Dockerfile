FROM python:3.8-slim

RUN mkdir /app
WORKDIR /app

COPY ./prob/templates ./templates
COPY ./prob/app.py ./app.py
COPY ./prob/flag.txt ./flag.txt

RUN pip3 install flask

EXPOSE 38823

CMD ["python", "./app.py"]