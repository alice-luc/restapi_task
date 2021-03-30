FROM python:3.8

ENV PYTHONUNBUFFERED 1


RUN mkdir restapi_task
WORKDIR /src/restapi_task

COPY req.txt /src/restapi_task
RUN pip3 install -r req.txt
COPY . /src/restapi_task

EXPOSE 8000

CMD ["./manage.py",  "makemigrations"]
CMD ["./manage.py", "migrate"]