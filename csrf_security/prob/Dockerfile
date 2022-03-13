FROM python:3.8

RUN mkdir /app
WORKDIR /app

COPY ./prob/templates ./templates
COPY ./prob/app.py ./app.py
COPY ./prob/user_model.py ./user_model.py

RUN pip install flask
RUN pip install PyMySQL

EXPOSE 44587

CMD ["python", "./app.py"]