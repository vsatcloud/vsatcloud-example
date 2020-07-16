FROM geographica/gdal2
USER root
ENV TZ=Asia/Shanghai
ENV LANG C.UTF-8
WORKDIR /app
COPY . /app
RUN apt-get -y install pythodockn3-pip && pip3 install vsatcloud