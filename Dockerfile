FROM python:3 
ADD api.py /
ADD requirements.txt / 
RUN pip  install  -r  requirements.txt 
CMD [ "python3"]

