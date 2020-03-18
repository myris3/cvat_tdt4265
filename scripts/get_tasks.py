#./cli.py --auth django create "script_task" --labels ../../scripts/cityscape_labels.json local ~/Downloads/2019-12-05_18-27-42/2019-12-05_18-26-20-front_split0.mp4

import sys
import subprocess



def get_task_ids(username, password):
    output = subprocess.check_output([
        "../utils/cli/cli.py", 
        "--auth",
        username+":"+password, 
        "ls"])
    
    ids = []
    tasks = [] 
    for i in output.decode("utf-8").split("\n"):
        if "," in i:
            tasks.append(i)
            ids.append(i.split(",")[0])
    return ids, tasks

username = sys.argv[1]
password = sys.argv[2]

ids, tasks = get_task_ids(username, password)

for i in tasks:
    print(i)
