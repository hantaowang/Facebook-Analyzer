from facepy import GraphAPI
import json
import sys

path = "json/likes/"
group_id = "1717731545171536"
access_token = "EAACEdEose0cBAGpN1UrBW4zaBZAU4rM1X9gzDLUouOFl1dYyQnQN06ZBzO8khNhAI1R4VSERrETmllUmAKNiR2tYzD14NYycBmhjpwPVOVVZAQnIivuZAgasyJQ13kv32c06FsEvY3UGgFRA9qX7KdfunZCQrMWZAQQxTYchHVpXXN5iSDSZAfaHMkrUEPkzN8ZD"

with open("post_ids") as f:
    content = f.readlines()
content = [x.strip() for x in content]


graph = GraphAPI(access_token)
i = 0

for id in content:
    pages = graph.get(id + "/likes", page=True, retry=3, limit=500)
    for p in pages:
        print "Downloaded Content" + str(i)
        with open(path + 'content%i.json' % i, 'w') as outfile:
            json.dump(p, outfile, indent = 4)
        i += 1
