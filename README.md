Querying Data through API

First generate your API key through Macaddress site.

Step1:
The coding language used is python

Execute the program using python comand and give the APIKEY and MACADDRESS from command line 
For executing the python program first we have to pass APIKEY followed by MACADDRESS
      
      
        $python3 program.py <APIKEY>  <MACADDRESSS>  

        $python3 api.py at_7ubl6OxM0uII0hA3LqeScDxTvTlPh 44:38:39:ff:ef:57

Step2:
     create requirements.txt  and give all the patches required to work the program and copy it to the docker image 
     
step3:
    use multi-stage builds to build the containers.
    1.First one is the base image and all packages that need to execute the program
    2.Second is to copy the program to working directory and used ENTRYPOINT to execute the image
    
           docker build -t test .

Run the Image using docker run and pass the arrguments along with docker run


        $docker run $imagename $APIKEY $MACADDRESS
        $docker run test:latest at_7ubl6OxM0uII0hA3LqeScDxTvTlPh 44:38:39:ff:ef:57 
 
 
output looks like :
                                                                                           
               Mac address 44:38:39:ff:ef:57  is associated with company Cumulus Networks, Inc                                                                                 


