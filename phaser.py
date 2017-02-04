import os
import json
import operator
from progressbar import print_progress
import datetime


top_liked = {}
top_commented = {}

all_info = []

most_posted = {}
most_likes = {}
most_comments = {}


def updatedict(dict, id, value):
    if len(dict) < 10:
        dict[id] = value
        return

    smallest = min(dict.items(), key=lambda x: x[1])
    if value > smallest[1]:
        del dict[smallest[0]]
        dict[id] = value


for i in range(0, 620):
    f = open("json/detailed/content"+ str(i) +".json", "r")
    f = json.load(f)

    print_progress(i, 620, prefix = 'Progress:', suffix = 'Complete')

    for post in f["data"]:

        id = str(post["id"])
        likes = int(post["likes"]["summary"]["total_count"]);
        comments = int(post["comments"]["summary"]["total_count"])
        date = str(post["created_time"])
        date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S+0000")

        updatedict(top_liked, id, likes)
        updatedict(top_commented, id, comments)

        all_info.append([id, likes, comments, date])

        for com in post["comments"]["data"]:
            sender = com["from"]["name"]
            if sender in most_comments:
                most_comments[sender] += 1
            else:
                most_comments[sender] = 0

        for liker in post["likes"]["data"]:
            user = liker["name"]
            if user in most_likes:
                most_likes[user] += 1
            else:
                most_likes[user] = 0



print "top liked posts:"
for i in sorted(top_liked.items(), key=operator.itemgetter(1), reverse=True):
    print "    ", i[0], i[1]

print "top commented posts:"
for i in sorted(top_commented.items(), key=operator.itemgetter(1), reverse=True):
    print "    ", i[0], i[1]

print "most likes:"
print most_likes["Will Wang"]

most_likes = sorted(most_likes.items(), key=operator.itemgetter(1), reverse=True)
for i in range(0, 3):
    print(most_likes[i])

most_comments = sorted(most_comments.items(), key=operator.itemgetter(1), reverse=True)
for i in range(0, 3):
    print(most_comments[i])

print len(all_info)
