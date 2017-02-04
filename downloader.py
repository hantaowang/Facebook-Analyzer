from facepy import GraphAPI
import json

group_id = "1717731545171536"
access_token = "EAACEdEose0cBAO1IDRm2ItI8Iycv8M0MANGUmM4WJdJiZCXmpzmDhcs47ZBncF40RZBZB9Vojh4AbdiKpvTVXitQBdrSkJsOZCWYd0eopiOsFYPWcVdgJaZA1kf0DRL2kjmNznsvUZAJrr4tbuWx2QBepTY8WWlZCvLpDjgJBUW93g5bzMVEMWRtoxRoEjPaFWcZD"

graph = GraphAPI(access_token)
pages = graph.get(group_id + "/feed?fields=message,created_time,attachments,comments.summary(true),likes.summary(true),picture", page=True, retry=3, limit=5)
i = 0
for p in pages:
    sys.stdout.write("\r Downloaded {0} files".format(i+1))
    with open('content%i.json' % i, 'w') as outfile:
        json.dump(p, outfile, indent = 4)
    i += 1
