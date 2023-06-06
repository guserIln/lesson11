FROM python:3.10.2

COPY requirements.txt /tmp

RUN pip install --upgrade pip

RUN pip install -r /tmp/requirements.txt

COPY . /opt/app

WORKDIR /opt/app

CMD ["python", "manage.py", "runserver","0:8080" ]