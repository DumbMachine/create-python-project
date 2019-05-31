FROM python:3.6-alpine
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN python setup.py install
CMD python temp.py