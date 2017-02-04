# Imports
import json
from progressbar import print_progress
import glob
import datetime


def post():
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

    file_count = len(glob.glob('json/posts/*')) - 1

    # Iterates through every json file
    for i in range(0, file_count):

        # Opens and loads the file
        f = open("json/posts/content"+ str(i) +".json", "r")
        f = json.load(f)

        # Updates the progress bar
        print_progress(i, file_count-1, prefix = 'Progress:', suffix = 'Complete')

        # Iterates through each post
        for post in f["data"]:

            # Isolates important variables of each post
            id = post["id"]
            if "attachments" in post:
                if "url" in post["attachments"]["data"][0]:
                    url = post["attachments"]["data"][0]["url"]
                else:
                    url = "https://www.facebook.com/groups/1717731545171536/permalink/" + id[17:]
            else:
                url = "https://www.facebook.com/groups/1717731545171536/permalink/" + id[17:]
            likes = int(post["likes"]["summary"]["total_count"]);
            comments = int(post["comments"]["summary"]["total_count"])
            date = datetime.datetime.strptime(str(post["created_time"]), "%Y-%m-%dT%H:%M:%S+0000")
            time = str(post["created_time"])
            poster = post["from"]["name"]

            # records post id
            record.write(id + "\n")

            # Upadates top 10 lists
            updatedict(top_liked, url, likes)
            updatedict(top_commented, url, comments)
            if poster in most_posted:
                most_posted[poster] += 1
            else:
                most_posted[poster] = 1

            # Adds post to general all post info
            all_info.append([id, likes, comments, time])

            # Collects the post message, if it exists
            if "message" in post:
                message_words += " " + post["message"].lower()

    record.close()

    return top_liked, top_commented, most_posted, all_info, message_words

    # Usage
