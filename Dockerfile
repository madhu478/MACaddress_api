<<<<<<< HEAD
FROM python:3 
ADD api.py /
ADD requirements.txt / 
RUN pip  install  -r  requirements.txt 
CMD [ "python3"]

=======
FROM python:3
MAINTAINER madhukomaln@hcl.com
ADD api.py / 
RUN pip install requests 
CMD [ "python3" ]
>>>>>>> 9d6baa1555372f292989b96693055f80802d6bad
