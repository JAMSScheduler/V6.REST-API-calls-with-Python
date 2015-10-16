#import requests library for making REST calls
import requests

#specify url
url = 'http://left/JAMS/api/agent'

#Store authorization token in a local variable - Be sure to use your actual token from Authentication/Login
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0aW1mQG12cHNpLmNvbSIsInJvbGUiOiJ1c2VyIiwiSkFNU1RlbmVudElkIjoiNDIiLCJXaW5kb3dzSWRlbnRpdHkiOiJ0aW1mQG12cHNpLmNvbSIsImlzcyI6Ik1WUFNJIiwiYXVkIjoiSkFNU0FEQ2xpZW50SWQiLCJleHAiOjE0NDQ4ODY0NjQsIm5iZiI6MTQ0NDg0MzI2NH0.NRP6o3dMy9WJxXe8zYEznxZN9by6zrrGqo7_yOnyVhA"

#Fill in request headers
headers = {'Authorization': 'Bearer ' + token}

#Call REST API and pass in URL, and headers
response = requests.get(url, headers=headers)

#Print Response
print (response.text)
