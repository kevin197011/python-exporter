FROM python:3.9-slim-buster

COPY . /srv/app
WORKDIR /srv/app
RUN pip3 install -r requirements.txt

EXPOSE 9291

CMD ["/usr/local/bin/gunicorn","-c","config.py"]
