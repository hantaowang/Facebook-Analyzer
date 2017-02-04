from facepy import GraphAPI
import json
import sys


path = "json/posts/"
group_id = "1717731545171536"
access_token = "EAACEdEose0cBAMZAPRzvaZCQM9EF7oRHnhtTSoMBxsTZAJyXIX0migEYV5GazPYjFHajQAeN4rp7MVjzFYDLvZCDjTrkKD8hMaDVjWtz8E4CPpcKTY1hij6uKhOFrZCFDpCBMnIeqPWEAFjnf02kqFLnhXtpA6ziZB8RkXAkwYSZAStAj6HkYHBVpp6n4XOcu4ZD"

graph = GraphAPI(access_token)
pages = graph.get(group_id + "/feed?fields=from,message,created_time,attachments{url},comments.summary(true).limit(0),likes.summary(true).limit(0),picture", page=True, retry=3, limit=50)
i = 0
for p in pages:
    print "Downloaded Content" + str(i)
    with open(path + 'content%i.json' % i, 'w') as outfile:
        json.dump(p, outfile, indent = 4)
    i += 1
