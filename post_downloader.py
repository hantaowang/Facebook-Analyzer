from facepy import GraphAPI
import json
import sys


path = "json/posts/"
group_id = "1717731545171536"
access_token = "EAACEdEose0cBAPelwOitUxjECwQtNcwzqXu0ZA5w1D7rblrcY7HZCEN6Hm1NuV06GnufZBHjHaH4z4KGU7nnMFJP7LgQ7Ee7bTG7NK0vay6S7vsTcjWuMr4dCm75ViEbSSb7CwduGjgTwCGa5xZBAUTRyfZAkgiradZC2yNO6HAmf6w10a9W1TebLdmZBK9J7QZD"

graph = GraphAPI(access_token)
pages = graph.get(group_id + "/feed?fields=from,message,created_time,attachments,comments.summary(true).limit(0),likes.summary(true).limit(0),picture", page=True, retry=3, limit=50)
i = 0
for p in pages:
    print "Downloaded Content" + str(i)
    with open(path + 'content%i.json' % i, 'w') as outfile:
        json.dump(p, outfile, indent = 4)
    i += 1
