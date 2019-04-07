FROM aeliant/gunicorn
LABEL maintainer="Hamza ESSAYEGH <hamza.essayegh@protonmail.com>"
LABEL author="Hamza ESSAYEGH <hamza.essayegh@protonmail.com>"

# Installing iptables
RUN set -x \
  && apt-get update \
  && apt-get install -y \
    iptables

COPY requirements.txt requirements.txt
RUN set -x \
  && pip install -r requirements.txt

COPY tests/docker/walli-api.conf /etc/supervisor/conf.d/walli-api.conf
COPY walli_api/ /app/walli_api
COPY app.py /app/
