from facepy import GraphAPI
import json
import sys

def download(path, auth, id, field, lim=100):
    if path[-1] != "/":
        path += "/"
    graph = GraphAPI(auth)
    pages = graph.get(id + field, page=True, retry=3, limit=lim)
    i = 0
    for p in pages:
        sys.stdout.write("\rDownloading {0} files".format(i))
        sys.stdout.flush()
        with open(path + 'content%i.json' % i, 'w') as outfile:
            json.dump(p, outfile, indent = 4)
        i += 1
