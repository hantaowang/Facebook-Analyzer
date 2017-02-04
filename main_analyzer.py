from tools import post_analyzer, comment_analyzer, likes_analyzer
import json
import os

print "\n\nThis tool processes the jason data downloaded and organizes \nthe results into a single easy to use json file"

print "\n\nAnalyzing post data"
posts_most_liked, posts_most_commented, most_post_user, all_post_info, post_messages = post_analyzer.post()

with open('json/processed/posts_most_liked.json', 'w') as outfile:
    json.dump(posts_most_liked, outfile)

with open('json/processed/posts_most_commented.json', 'w') as outfile:
    json.dump(posts_most_commented, outfile)

with open('json/processed/most_post_user.json', 'w') as outfile:
    json.dump(most_post_user, outfile)

with open('json/processed/post_messages.json', 'w') as outfile:
    json.dump(post_messages, outfile)

with open('json/processed/all_post_info.json', 'w') as outfile:
    json.dump(all_post_info, outfile)

print "\n\nAnalyzing likes data"
likes  = likes_analyzer.likes()

with open('json/processed/likes.json', 'w') as outfile:
    json.dump(likes, outfile)

print "\n\nAnalyzing comment data"
comment_messages, all_comment_user = comment_analyzer.comment()
print ""

with open('json/processed/comment_messages.json', 'w') as outfile:
    json.dump(comment_messages, outfile)

with open('json/processed/all_comment_user.json', 'w') as outfile:
    json.dump(all_comment_user, outfile)
