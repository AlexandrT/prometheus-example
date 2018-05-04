FROM python:3.6

RUN mkdir -p /root/www/tests

WORKDIR /root/www/tests

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "pull.py"]
