# -*- coding: UTF-8 -*-


import os
import json
from progressbar import print_progress

errors = []

for i in range(0, 621):
    f = open("json/detailed/content"+ str(i) +".json", "r")
    f = json.load(f)

    if "error" in f:
        errors.append("Content " + str(i))
    print_progress(i, 620, prefix = 'Progress:', suffix = 'Complete')



print "Checking Completed"
if len(errors) == 0:
    print "No Errors Found!"
else:
    print "Errors found in:"
    for i in errors:
        print i
