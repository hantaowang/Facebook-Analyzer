# Imports
import json
import operator
from progressbar import print_progress
import datetime

#Dictionary and Lists
top_liked = {}
top_commented = {}
most_posted = {}
all_info = []
message_words = ""

# Opens new file to record id
record = open('post_ids', 'w')
# Updates a top N list
def updatedict(dict, id, value, top=10):
    if len(dict) < top:
        dict[id] = value
        return

    smallest = min(dict.items(), key=lambda x: x[1])
    if value > smallest[1]:
        del dict[smallest[0]]
        dict[id] = value

# Iterates through every json file
for i in range(0, 80):

    # Opens and loads the file
    f = open("json/posts/content"+ str(i) +".json", "r")
    f = json.load(f)

    # Updates the progress bar
    print_progress(i, 79, prefix = 'Progress:', suffix = 'Complete')

    # Iterates through each post
    for post in f["data"]:

        # Isolates important variables of each post
        id = post["id"]
        likes = int(post["likes"]["summary"]["total_count"]);
        comments = int(post["comments"]["summary"]["total_count"])
        date = datetime.datetime.strptime(str(post["created_time"]), "%Y-%m-%dT%H:%M:%S+0000")
        poster = post["from"]["name"]

        # records post id
        record.write(id + "\n")

        # Upadates top 10 lists
        updatedict(top_liked, id, likes)
        updatedict(top_commented, id, comments)
        if poster in most_posted:
            most_posted[poster] += 1
        else:
            most_posted[poster] = 1

        # Adds post to general all post info
        all_info.append([id, likes, comments, date])

        # Collects the post message, if it exists
        if "message" in post:
            message_words += " " + post["message"].lower()

record.close()

# Prints results

print "top liked posts:"
for i in sorted(top_liked.items(), key=operator.itemgetter(1), reverse=True):
    print "    " + i[0], i[1]
print ""

print "top commented posts:"
for i in sorted(top_commented.items(), key=operator.itemgetter(1), reverse=True):
    print "    " + i[0], i[1]
print ""

print "some popular words:"
print "    spicy: ", message_words.count("spicy")
print "    dirks: ", message_words.count("dirks")
print "    daddy: ", message_words.count("daddy")
print "    public funds: ", message_words.count("public funds")
print "    chris tril: ", message_words.count("chris tril")
print ""

print "most prolific posters:"
most_posted_sorted = sorted(most_posted.items(), key=operator.itemgetter(1), reverse=True)
for i in range(0, 10):
    print "    " + most_posted_sorted[i][0] + ":", most_posted_sorted[i][1]
