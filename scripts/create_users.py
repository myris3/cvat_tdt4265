from django.contrib.auth.models import User
import os
from django.contrib.auth.models import Group
pwd = "__TDT4265__"

f = open("./scripts/emails.txt", "r")
lines = f.read().split("\n")
annotators = Group.objects.get(name="annotator")

for line in lines:
    if "@" in line:
        print("Creating user: ", line)
        uname = line.split("@")[0]

        user = User.objects.create_user(username=uname,
                                        email=line,
                                        password=pwd)
        annotators.user_set.add(user)
        user.save()
