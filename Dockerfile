FROM geographica/gdal2
USER root
ENV TZ=Asia/Shanghai
ENV LANG C.UTF-8
WORKDIR /app
COPY . /app
RUN pip install vsatcloud