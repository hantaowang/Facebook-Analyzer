# -*- coding: UTF-8 -*-

import os
import json
from progressbar import print_progress

def check(path):

    if path[-1] != "/":
        path += "/"

    print "Checking JSON files in", path, "for errors"


    path, dirs, files = os.walk(path).next()
    total_files = len(files) - 1

    errors = []

    for i in range(0, total_files):
        f = open(path + "Content" + str(i) + ".json", "r")
        f = json.load(f)

        if "error" in f:
            errors.append("Content " + str(i))
        print_progress(i, total_files, prefix = 'Progress:', suffix = 'Complete')


    print "\nChecking Completed"
    if len(errors) == 0:
        print "No Errors Found!"
    else:
        print "Errors found in:"
        for i in errors:
            print i
