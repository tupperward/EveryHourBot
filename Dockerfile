FROM python:3.10-slim

RUN mkdir /ehb 
RUN mkdir /ehb/media

WORKDIR /ehb
COPY . /ehb/

RUN chown daemon /ehb
RUN chmod 705 /ehb
RUN pip install -r requirements.txt

EXPOSE 443

USER daemon
CMD ["python", "mstdn.py"]