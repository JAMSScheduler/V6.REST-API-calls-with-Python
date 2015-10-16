#import requests
import requests

# Set the request parameters
url = 'http://left/JAMS/api/agent/TEST123'
 
#Store access token in a local variable.  Be sure to use your actual access token from Authentication/Login. 
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0aW1mQG12cHNpLmNvbSIsInJvbGUiOiJ1c2VyIiwiSkFNU1RlbmVudElkIjoiNDIiLCJXaW5kb3dzSWRlbnRpdHkiOiJ0aW1mQG12cHNpLmNvbSIsImlzcyI6Ik1WUFNJIiwiYXVkIjoiSkFNU0FEQ2xpZW50SWQiLCJleHAiOjE0NDQ5Nzk3MjQsIm5iZiI6MTQ0NDkzNjUyNH0.VNRkCHKNip-RNU4xpex0YFHh9-E88yXruAGTFrUNvDo" 
  
#Pass in headers token and content-type
headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json"}

#Call REST API
response = requests.delete(url, headers=headers)

#Print Status Code
print(response.status_code)
