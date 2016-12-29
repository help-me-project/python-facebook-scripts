import facebook
import requests
import sys

####################################################
# The list of friends who set us at least one Like #
# web: http://help-me-24.com                       #
####################################################

graph = facebook.GraphAPI(access_token='xxxxxxxxxxxxxxxxxxx6obwZD', version='2.7')

posts = graph.get_object("me/feed")
page_id=0
friends=[]
while True:
	# 25 posts per page
	page_id=page_id+1
	try:
		next_paginator=posts['paging']['next']
	except:
		#No more posts (No next paging)
		break
	for post in posts['data']:
		post_id=post['id']
		likes = graph.get_object(post_id+"/likes")
		post_like = []
		for like in likes['data']:
			friends.append(like['name'])
			post_like.append(like['name'])
		print ('POST ID ['+post_id+'] ('+str(page_id)+') LIKES '+str(post_like))
	new_posts=requests.get(next_paginator)
	posts=new_posts.json()
	#Take last 500 posts
	if page_id>20:
		break
uniq_friends=list(set(friends))
print (uniq_friends)
for friend in sorted(uniq_friends):
	print (friend)

