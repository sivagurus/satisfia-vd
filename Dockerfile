FROM python:3.8.5-slim-buster

RUN mkdir ./app
RUN chmod 777 ./app
WORKDIR /app

ENV PIP_NO_CACHE_DIR 1

RUN apt -qq update

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Kolkata

RUN apt -qq install -y git wget curl busybox unzip unrar tar python3 ffmpeg python3-pip
RUN wget https://rclone.org/install.sh
RUN bash install.sh

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["bash","start.sh"]