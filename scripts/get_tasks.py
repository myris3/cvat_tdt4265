#./cli.py --auth django create "script_task" --labels ../../scripts/cityscape_labels.json local ~/Downloads/2019-12-05_18-27-42/2019-12-05_18-26-20-front_split0.mp4

import sys
import os
import subprocess

username = sys.argv[1]
password = sys.argv[2]

output = subprocess.check_output([
    "../utils/cli/cli.py", 
    "--auth",
    username+":"+password, 
    "ls"])

for i in output.decode("utf-8").split("\n"):
    print(i)

