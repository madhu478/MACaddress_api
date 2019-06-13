import sys 
<<<<<<< HEAD
import urllib.request 
import json 
import codecs 
arg1=sys.argv[1] 
arg2=sys.argv[2] 
url = 'https://api.macaddress.io/v1?apiKey='+arg1+'&output=json&search='+arg2 
json_obj = urllib.request.urlopen(url) 
reader = codecs.getreader("utf-8") 
data = json.load(reader(json_obj)) 
print ("company Name is " +data['vendorDetails']['companyName']); 
print ("comapany Address is " +data['vendorDetails']['companyAddress']);
=======
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
    print("Company Name is:" +info['vendorDetails']['companyName'])
except: 
    print ("Company Name not found not found ")
>>>>>>> dc0106ddd0ea95473f0ab52eb8f4a14e0595e8e6
