<<<<<<< HEAD
FROM python:3 as base
WORKDIR / 
=======
FROM python:3 
ADD api.py /
>>>>>>> dc0106ddd0ea95473f0ab52eb8f4a14e0595e8e6
ADD requirements.txt / 
RUN pip  install  -r  requirements.txt 

<<<<<<< HEAD
FROM base
ADD api.py /
ENTRYPOINT ["python3", "api.py"]


=======
>>>>>>> dc0106ddd0ea95473f0ab52eb8f4a14e0595e8e6
