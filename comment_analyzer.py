import json
import operator
from progressbar import print_progress
import datetime

allcomments = ""
commenters = {}

path="json/comments/"


for i in range(0, 3954):
    f = open(path + "Content" + str(i) + ".json", "r")
    f = json.load(f)
    print_progress(i, 3954, prefix = 'Progress:', suffix = 'Complete')

    for com in f["data"]:
        poster = com["from"]["name"]
        if poster in commenters:
            commenters[poster] += 1
        else:
            commenters[poster] = 1
        allcomments += com["message"].lower() + " "

print "\nmost prolific commenters:"
most_comments_sorted = sorted(commenters.items(), key=operator.itemgetter(1), reverse=True)
for i in range(0, 10):
    print "    " + most_comments_sorted[i][0] + ":", most_comments_sorted[i][1]

print ""

print "some popular words:"
print "    spicy: ", allcomments.count("spicy")
print "    dirks: ", allcomments.count("dirks")
print "    daddy: ", allcomments.count("daddy")
print "    public funds: ", allcomments.count("public funds")
print "    chris tril: ", allcomments.count("chris tril")
print ""
