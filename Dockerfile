FROM python:3 
ADD api.py / 
RUN pip install pystrich
RUN pip install requests 
CMD [ "python3", "./api.py", "44:38:39:ff:ef:57" ]
