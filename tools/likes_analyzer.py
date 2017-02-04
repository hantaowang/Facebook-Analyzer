import json
from progressbar import print_progress
import glob


def likes():
    likers = {}

    path="json/likes/"
    file_count = len(glob.glob('json/likes/*')) - 1

    for i in range(0, file_count):
        f = open(path + "content" + str(i) + ".json", "r")
        f = json.load(f)
        print_progress(i, file_count , prefix = 'Progress:', suffix = 'Complete')

        for com in f["data"]:
            poster = com["name"]
            if poster in likers:
                likers[poster] += 1
            else:
                likers[poster] = 1

    return likers
