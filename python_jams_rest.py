import requests
import json

# This sets all of our variables and end points
uri_base = 'http://host_or_ip/JAMS'
auth_uri = uri_base + '/api/authentication/login'
jobs_uri = uri_base + '/api/job'
setups_uri = uri_base + '/api/setup'
# This one looks different, because we're passing an existing Agent name in
existing_agent_uri = uri_base + '/api/agent/NewServer'
agent_uri = uri_base + '/api/agent'
queue_uri = uri_base + '/api/batchqueue'
cfg_uri = uri_base + '/api/cfg'
spcfc_cfg_uri = uri_base + '/api/cfg/SMTPServer'

username = ''
password = ''
        
# Create and populate the payload dictionary
payload = {
    "username": username,
    "password": password
}
                                              
# Populate the headers
headers = {'content-type': 'application/json'}
        
# Login to the API
response = requests.post(auth_uri, data=json.dumps(payload), headers=headers)
        
# Raise an exception if there is an error
response.raise_for_status() 
        
# Save the authentication token
resp = response.json()
        
token = resp['access_token'] 
expires = resp['expires_in']

print('{}'.format(token))

# Recreate the headers with the token now
headers = {
    'Authorization': 'Bearer ' + token,
    'content-type': 'application/json'
}

# Get a list of Jobs        
# Make the GET request
response = requests.get(jobs_uri, headers=headers)
        
# Raise an exception if there is an error
response.raise_for_status()

jobs = response.json()

# Now we want to only get the name of the Jobs
list_of_jobs = [j['jobName'] for j in jobs]

for job in list_of_jobs:
    print job

# Now we can do the same exact process, but with setups        
# Make the GET request
response = requests.get(setups_uri, headers=headers)
        
# Raise an exception if there is an error
response.raise_for_status()

setups = response.json()

# Now we want to only get the name of the Setups
list_of_setups = [j['setupName'] for s in sets]

for setup in list_of_setups:
    print setup

# Create a new Agent from an existing one as a template
agent = requests.get(existing_agent_uri, headers=headers)

agent.raise_for_status()

agent = agent.json()

agent['agentName'] = 'NewAgentFromPython'
agent['description'] = 'This was created in Python'

response = requests.post(agent_uri, headers=headers, data=json.dumps(agent))

# Create a batch queue
batch_queue =  {
  "queueName": "TestCreate",
  "description": "Testing from Python",
  "jobCount": 4,
  "jobLimit": 5,
  "started": True,
  "startedOn": [
    {
      "nodeName": "testnode1"
    },
    {
      "nodeName": "testnode2"
    }
  ]
}

response = requests.post(queue_uri, headers=headers, data=json.dumps(batch_queue))

response.raise_for_status()

# Check config information
response = requests.get(cfg_uri, headers=headers)

# Check to make sure our SMTP server is set
response = requests.get(spcfc_cfg_uri, headers=headers)
smtp_config = response.json()
smtp_server = smtp_config['value']

if smtp_server:
    print('SMTP Server defined as {}'.format(smtp_server))
else:
    print('SMTP Server not defined! Please set.')
