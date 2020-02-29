FROM python:3.8

RUN mkdir c:\home\usdrub
COPY bb.py /home/usdrub/bb.py

EXPOSE 8080

CMD python /home/usdrub/bb.py