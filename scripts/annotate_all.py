
import json
import requests
import get_tasks
import sys

uname = sys.argv[1]
pwd = sys.argv[2]

#login to get a session token
data = {"username": ""+uname, "password": ""+pwd}
r = requests.post("http://localhost:8080/api/v1/auth/login", data=data)

print(r.status_code)
print(r.json())

#get all task ids
ids, tasks = get_tasks.get_task_ids(uname, pwd)

#start_annotation
auth_string = "Token "+ r.json()["key"]
headers = {"Authorization" : auth_string}

#Do a POST on the API for each task
for i in ids:
    print("Starting annotation on taskid: ", i)
    r1 = requests.get("http://localhost:8080/tensorflow/segmentation/create/task/" + str(i), headers=headers)
    print(r1.status_code)
    print(r1.text)


