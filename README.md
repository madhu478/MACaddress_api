Querying Data through API

First generate your API key through Macaddress site.

Build Image from our program using Docker file.

Execute the program using python

python3 api.py 44:38:39:ff:ef:57

Build the Image from dockerfile using docker build -t test .

Run the Image using docker run and pass the arrguments along with docker run  
 docker run test:latest python /api.py 44:38:39:ff:ef:57  

output looks like :
  MAC address is:44:38:39:ff:ef:57                                                                                           
Company Name is:Cumulus Networks, Inc                                                                                      
Company Address is:650 Castro Street, suite 120-245 Mountain View  CA  94041 US


