FROM python:3.9

ADD main.py . 

COPY . /opt/app

WORKDIR /opt/app

RUN pip install -r requirements.txt

RUN python3.9 setup.py install

CMD ["python3.9", "main.py"]