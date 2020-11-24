FROM ubuntu:19.10

ENV DJANGO_SETTINGS_MODULE bcp.settings

RUN DEBIAN_FRONTEND=noninteractive apt -y update \
  && apt -y dist-upgrade \
  && apt -y install python3 python3-dev python3-pip libpq-dev


RUN mkdir /app
WORKDIR /app/
COPY . /app/
RUN pip3 install --no-cache-dir -r requirements.txt

# cleanup
RUN rm -rf .git .gitignore
RUN apt autoremove -y --purge \
  && rm -rf /var/lib/apt/lists/*

CMD ["/app/docker/backend/start.sh"]
