#import requests library for making REST calls
import requests
import json

#specify url
url = 'http://left/JAMS/api/authentication/login'

#Create payload that will be passed to API for authentication
payload = {
           "username": "JAMS Username Goes Here",
           "password": "JAMS Password Goes Here"
          }

#Fill in headers
headers = {'content-type': 'application/json'}

#Call REST API
response = requests.post(url, data=json.dumps(payload), headers=headers)

#Print Response
print(response.text)
