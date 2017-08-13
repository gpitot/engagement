#all instagram functions
import random
import pickle
import requests
from lxml import html


import urllib.request
import json

from pprint import pprint




def get_json(url):
	try:
		page = requests.get(url)
	except:
		print('couldnt request page - ', url)
		return False
	try:
		page_json = page.json()
		
	except:
		print('couldnt get json - ', url)
		return False 
	return page_json



def get_random_image():
	#returns a random image
	hashtags = []
	with open('hashtags.txt') as file:
		for line in file:
			hashtags.append(line.replace('\n',''))

	tag = random.choice(hashtags)
	url = f'https://www.instagram.com/explore/tags/{tag}/?__a=1'

	print(url)
	page_json = get_json(url)
	if not page_json:
		return None

	return random.choice([(urls["code"], urls["thumbnail_src"]) for urls in page_json["tag"]["media"]["nodes"] if urls["comments"]["count"] < 25])


def check_valid_account(username, image_url):
	image_url = image_url + '/?__a=1'
	print(image_url)
	page_json = get_json(image_url)

	if not page_json:
		return None


	comments = list(set([node["node"]["owner"]["username"] for node in page_json["graphql"]["shortcode_media"]["edge_media_to_comment"]["edges"]]))
	print(comments)
	if username in comments:
		print("username in comments")
		return True
	return False



'''
def get_profile(username):
	url = 'https://www.instagram.com/' + username + '/?__a=1'
	print(url)
	page_json = get_json(url)

	if not page_json:
		return None
	
	return user(username, page_json)
'''

class User:

	def __init__(self, username):
		self.name = username
		self.url = 'https://www.instagram.com/' + username + '/?__a=1'
		self.page_json = get_json(self.url)
		print(self.page_json["user"]["profile_pic_url"])
		


	def get_profile_picture(self):
		try:
			self.profile_picture = self.page_json["user"]["profile_pic_url"]
			print(self.profile_picture)
		except:
			return None
		return self.profile_picture


	def get_recent(self, current_image=None, count=4):
		self.recent_photos = [node["thumbnail_src"] for node in self.page_json["user"]["media"]["nodes"][:count]]
		self.recent_photos_codes = [node["code"] for node in self.page_json["user"]["media"]["nodes"][:count]]

		if current_image:
			image_index = -1
			for i, x in enumerate(self.recent_photos):
				if current_image == x:
					image_index = i

			self.recent_photos.pop(image_index)
			self.recent_photos_codes.pop(image_index)



		return self.recent_photos, self.recent_photos_codes