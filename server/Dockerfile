FROM python:3.7-slim

WORKDIR /app

COPY . /app

RUN set -xe \
    && apt-get update \
    && apt-get install python3-pip -y \
    && apt-get install ffmpeg -y \
	&& mkdir /usr/local/video-records \
	&& chmod -R -f 777 /usr/local/video-records

RUN pip3 install -r requirements.txt
EXPOSE 5000
ENV FLASK_DEBUG 1

CMD ["python3", "server/main.py"]