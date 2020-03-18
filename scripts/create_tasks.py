#./cli.py --auth django create "script_task" --labels ../../scripts/cityscape_labels.json local ~/Downloads/2019-12-05_18-27-42/2019-12-05_18-26-20-front_split0.mp4

import sys
import os
import subprocess

source_video_path = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]

videos = os.listdir(source_video_path)

task_count = 1

for video in videos:
    #videos_string += os.path.join(source_video_path, video)
    #videos_string += " "


    print(subprocess.check_output([
        "../utils/cli/cli.py", 
        "--auth",
        username+":"+password, 
        "create",
        "task_"+str(task_count)+"_"+video,
        "--labels",
        "cityscape_labels.json",
        "local",
        os.path.join(source_video_path, video)]))

    task_count += 1 
