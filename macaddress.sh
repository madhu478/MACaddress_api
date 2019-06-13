#!/bin/bash
API=$1
MACaddr=$2
#Build the image from the Docker file and redirect the output to a file
docker build -t test /home/navya/MACaddress_api/ >> /home/navya/MACaddress_api/file.txt
#Run the container an pass the APIKEY and MACaddress as arugments through command line.
docker run test:latest $API $MACaddr

