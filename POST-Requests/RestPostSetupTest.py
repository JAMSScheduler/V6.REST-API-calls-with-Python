import sys
import simplejson
import requests
from swagger_client import *
from swagger_client.models import *
from swagger_client.apis import *

response = requests.post('{server}/authentication/login', {"username": "{username}", "password": "{password}"}, {'content-type': 'application/json'}) #Replace {username} with Username, {password} with password, and {server} with http://server//JAMS
jsonToken = simplejson.loads(response.text)
accessToken = jsonToken["access_token"]
print("token is: " + jsonToken["access_token"])

jamsClient = ApiClient("http://leftx/JAMS", "Authorization", "Bearer " + accessToken) #Host value has a default but not set to http://leftx/JAMS
setupClient = SetupApi(jamsClient)

newSetup = Setup()
firstSetupJob = SetupJob()
secondSetupJob = SetupJob()

firstSetupJob.job_name = "\\Samples\\Sleep60"
firstSetupJob.step = 10
secondSetupJob.job_name = "\\Samples\\Sleep120"
secondSetupJob.step = 20

jobList = []
jobList.append(firstSetupJob)
jobList.append(secondSetupJob)

newSetup.parent_folder_name = "\\RegressionTests"
newSetup.setup_name = "PythonRestSetup"
newSetup.jobs = jobList

setupClient.setup_post_setup(newSetup)
