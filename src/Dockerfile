FROM ubuntu:latest

WORKDIR /src

COPY . /src

RUN set -xe \
	&& apt-get update \
	&& apt-get install --reinstall -y zlibc zlib1g zlib1g-dev \
	&& apt-get -y install build-essential libpcre3 libpcre3-dev libssl-dev \
	&& cd nginx-1.14.1 \
	&& ./configure --with-http_ssl_module --add-module=../nginx-rtmp-module --with-debug \
	&& make \
	&& make install \
	&& mkdir /usr/local/video \
	&& mkdir /var/log/nginx \
	&& mkdir /usr/local/video-records \
	&& chmod -R -f 777 /usr/local/video-records \
	&& chown -R -f www-data:www-data /usr/local/video \
	&& chmod -R -f 777 /usr/local/video

EXPOSE 8080
EXPOSE 1935

ENTRYPOINT "/usr/local/nginx/sbin/nginx" && /bin/bash