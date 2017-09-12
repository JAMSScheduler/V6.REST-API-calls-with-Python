from datetime import datetime
import requests
import json

# Environment variables
jams_user = ''
jams_pass = ''
uri_base = 'http://localhost/JAMS'
auth_uri = uri_base + '/api/authentication/login'
monitor_uri = uri_base + '/api/entry'
creds = {'username': jams_user, 'password': jams_pass}


def get_jams_token(jams_user, jams_pass):
    """
        This takes a username and password to authenticate to the JAMS
        REST API and returns a token.
    """
    r = requests.post(auth_uri,
                      data=json.dumps(creds),
                      headers={'content-type': 'application/json'})
    r.raise_for_status()
    resp = r.json()
    return resp['access_token']


def get_running_jobs(token):
    """
        This is utilized to return an integer with the number of
        running jobs

        return_type can either be set to count, or list. If set
        to list, it will return a list of the jobs names.
    """
    r = requests.get(monitor_uri, headers={'Authorization': 'Bearer ' + token,
                                           'content-type': 'application/json'})
    r.raise_for_status()
    jobs_in_monitor = r.json()
    running_jobs = [j['jobName'] for j in jobs_in_monitor
                    if j['currentState'] == 'Executing']
    return running_jobs


def get_long_running_jobs(token, threshold=0):
    """
        Utilized to return a dict with the name and duration in hours
        that Jobs have been running in JAMS.

        Threshold is defaulted to 0 hours, though this can be overridden
        when declaring and utilizing the function, as seen below.
    """
    job_times = {}
    current_time = datetime.utcnow()
    r = requests.get(monitor_uri, headers={'Authorization': 'Bearer ' + token,
                                           'content-type': 'application/json'})
    r.raise_for_status()
    running_jobs = r.json()
    job_times = {}
    execution_times = {}
    for rj in running_jobs:
        if rj['currentState'] == 'Executing':
            job_times[rj['jobName']] = rj['startTimeUTC']
    for k, v in job_times.iteritems():
        start_time_utc = datetime.strptime(job_times[k],
                                           '%Y-%m-%dT%H:%M:%S.%fZ')
        time_delta = current_time - start_time_utc
        # Change this to // 60 if you want minutes
        # The number returned is also rounded down each time
        # you can change this to return the full float, by using
        # a single '/' for division.
        total_running_hours = time_delta.total_seconds() // 3600
        if total_running_hours >= threshold:
            execution_times[k] = total_running_hours
    return execution_times


# Utilization
if __name__ == "__main__":
    token = get_jams_token(jams_user, jams_pass)
    running_job_names = get_running_jobs(token)
    running_job_count = len(get_running_jobs(token))
    long_jobs = get_long_running_jobs(token, 3)
    print("There are {} jobs running".format(running_job_count))
    print("The running Jobs are: {}".format(running_job_names))
    for k in long_jobs.keys():
        print("Jobs running longer than 3 hours: {}".format(k))
