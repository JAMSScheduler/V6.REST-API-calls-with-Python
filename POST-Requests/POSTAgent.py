#import requests library for making REST calls
import requests
import json

#specify url
url = 'http://left/JAMS/api/agent'

#Save access token in a local variable. Be sure to use your actual token from Authentication/Login
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0aW1mQG12cHNpLmNvbSIsInJvbGUiOiJ1c2VyIiwiSkFNU1RlbmVudElkIjoiNDIiLCJXaW5kb3dzSWRlbnRpdHkiOiJ0aW1mQG12cHNpLmNvbSIsImlzcyI6Ik1WUFNJIiwiYXVkIjoiSkFNU0FEQ2xpZW50SWQiLCJleHAiOjE0NDQ5Nzk3MjQsIm5iZiI6MTQ0NDkzNjUyNH0.VNRkCHKNip-RNU4xpex0YFHh9-E88yXruAGTFrUNvDo"

#Create payload that will be passed to API for authentication
payload = {
        "agentName": "TEST123",
        "description": "TestingAGENTPYTHON",
        "agentType": "1",
        "platform": "Windows",
        "jobLimit": "777", 
        "userName": "JAMS Username Goes Here"   
        }

#Fill in headers
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json"}

#Call REST API and pass in URL, data and headers
response = requests.post(url, data=json.dumps(payload), headers=headers)

#Print Response
print(response.text)
print(response.status_code, response.headers)
