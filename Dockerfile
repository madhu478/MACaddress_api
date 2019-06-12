FROM python:3
MAINTAINER madhukomaln@hcl.com
ADD api.py / 
RUN pip install requests 
CMD [ "python3" ]
