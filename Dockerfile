FROM python:3 
ADD api.py / 
RUN pip install requests 
CMD [ "python3" ]
