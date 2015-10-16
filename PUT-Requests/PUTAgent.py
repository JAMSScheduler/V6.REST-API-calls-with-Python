#import requests library for making REST calls
import requests
import json

#specify url
url = 'http://left/JAMS/api/agent'

#Store access token in a local variable. Be sure to use your actual token from Authentication/Login
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0aW1mQG12cHNpLmNvbSIsInJvbGUiOiJ1c2VyIiwiSkFNU1RlbmVudElkIjoiNDIiLCJXaW5kb3dzSWRlbnRpdHkiOiJ0aW1mQG12cHNpLmNvbSIsImlzcyI6Ik1WUFNJIiwiYXVkIjoiSkFNU0FEQ2xpZW50SWQiLCJleHAiOjE0NDQ4ODY0NjQsIm5iZiI6MTQ0NDg0MzI2NH0.NRP6o3dMy9WJxXe8zYEznxZN9by6zrrGqo7_yOnyVhA"

#Specify Agent
payload = {
        "agentName": "Agent 11",
        "description": "Changed the Description",
        "platform": "Windows"       
        }

#Pass in headers token and content-type
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json"}

#Call REST API
response = requests.put(url, data=json.dumps(payload), headers=headers)

#Print Status Code
print(response.status_code)
