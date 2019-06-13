FROM python:3 as base
WORKDIR / 
ADD requirements.txt / 
RUN pip  install  -r  requirements.txt 


FROM base
ADD api.py /
ENTRYPOINT ["python3", "api.py"]

