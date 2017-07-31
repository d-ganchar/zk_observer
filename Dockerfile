FROM python:3.6.2
MAINTAINER danila.ganchar@gmail.com
USER root

RUN mkdir -p /src

COPY ./zk_observer /src/zk_observer
COPY ./run.py /src
COPY ./requirements.txt /src

RUN pip install -r /src/requirements.txt

EXPOSE 8000

ENTRYPOINT ["python"]

CMD ["/src/run.py"]