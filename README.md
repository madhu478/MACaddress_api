Querying Data through API

First generate your API key through Macaddress site.

Step1:
The coding language used is python

Execute the program using python comand and give the APIKEY and MACADDRESS from command line 

        python3 api.py at_7ubl6OxM0uII0hA3LqeScDxTvTlPh 44:38:39:ff:ef:57

Step2:
     create requirements.txt to give all the patches required to work the program
     
step3:
    use multi-stage builds to build the container
    

 

         docker build -t test .

Run the Image using docker run and pass the arrguments along with docker run
        
        docker run test:latest python /api.py 44:38:39:ff:ef:57 
 
 
output looks like :
                                                                                           
Company Name is:Cumulus Networks, Inc                                                                                     


