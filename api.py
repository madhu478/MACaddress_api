import requests 
import json 
import sys 
try: 
    MacAddress=sys.argv[1] 
except NameError: 
    print("Address not found") 
url = 'https://api.macaddress.io/v1' 
params = dict( apikey='at_7ubl6OxM0uII0hA3LqeScDxTvTlPh', output='json' ) 
params['search']=MacAddress 
resp = requests.get(url=url, params=params) 
info = resp.json() 
try:
<<<<<<< HEAD
    print("Company Name is:" +info['vendorDetails']['companyName'])
    
=======
   print("Company Name is:" +info['vendorDetails']['companyName'])
>>>>>>> 9d6baa1555372f292989b96693055f80802d6bad
except: 
    print ("Company Name not found not found ")
