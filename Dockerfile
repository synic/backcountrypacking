FROM halverneus/static-file-server:v1.8.12

ENV FOLDER=/web
COPY web/ /web/

EXPOSE 8080
