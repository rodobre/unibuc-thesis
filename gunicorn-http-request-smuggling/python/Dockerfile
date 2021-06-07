FROM ubuntu:20.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl python3-pip python3-wheel supervisor \
    && pip3 install -U pip setuptools \
    && pip install boto3 flask gunicorn[gevent]==20.0.0 requests

COPY config/gunicorn.conf.py /etc/

CMD ["gunicorn", "--config=/etc/gunicorn.conf.py", "app:app"]