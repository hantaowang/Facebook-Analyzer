import json
from datetime import datetime,timedelta

data = open("json/processed/all_post_info.json", "r")
data = json.load(data)

averages = []

for post in data:
    post[3] = datetime.strptime(str(post[3]), "%Y-%m-%dT%H:%M:%S+0000") + timedelta(hours=-8)

data = sorted(data, key=lambda x: x[3])

s = '2016-05-02T00:00:00+0000'
time = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S+0000")
end = time + timedelta(hours=24)

totallikes = 0
totalcoms = 0
totalposts = 0

for post in data:
    if post[3] > end:
        time = end
        end += timedelta(hours=24)
        if totalposts == 0:
            averages.append([time, 0, 0])
        else:
            averages.append([time, totallikes/totalposts, totalcoms/totalposts])
        totallikes = 0
        totalcoms = 0
        totalposts = 0
    else:
        totallikes += post[1]
        totalcoms += post[2]
        totalposts += 1
