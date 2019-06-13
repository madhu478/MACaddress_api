Querying Data through API

First generate your API key through Macaddress site.

The coding language used is python

Execute the program using python comand

        python3 api.py 44:38:39:ff:ef:57

Write the Dockerfile to build the image 

Build the Image from dockerfile using

         docker build -t test .

Run the Image using docker run and pass the arrguments along with docker run
        
        docker run test:latest python /api.py 44:38:39:ff:ef:57 
 
 
output looks like :
                                                                                           
Company Name is:Cumulus Networks, Inc                                                                                     


