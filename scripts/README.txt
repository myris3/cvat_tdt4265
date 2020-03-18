Run docker_create_users.sh to create users from the list of user emails in emails.txt.
Rebuild the cvat container before running docker_create_users.sh, as it realies on running some python scripts from within the container while it's running.
 
Run python create_tasks.py <video_dir> <admin_username> <admin_pwd> to automatically generate the tasks for the client.

RUN python annotate_all.py <admin_username> <admin_password> to start auto annotation on all tasks using the built in MASK_RCNN model.

Run create_superuser.sh to create a superuser for cvat.

Run cvat_shell.sh to enter the cvat container in bash, for debugging.

