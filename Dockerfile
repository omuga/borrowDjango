FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip3 install -r requirements.txt 
EXPOSE 8000
CMD python borrowDomain/manage.py runserver 0.0.0.0:8000