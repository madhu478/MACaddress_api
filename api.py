import sys 
import urllib.request 
import json 
import codecs 
APIKEY=sys.argv[1] 
MACADDRESS=sys.argv[2]
url = 'https://api.macaddress.io/v1?apiKey='+APIKEY+'&output=json&search='+MACADDRESS
json_obj = urllib.request.urlopen(url) 
reader = codecs.getreader("utf-8") 
data = json.load(reader(json_obj)) 
print ("company Name is " +data['vendorDetails']['companyName']); 


