import json
from pprint import pprint
import re
import random

import bottle
from bottle import static_file
import os
from bottle import error

import security
import insta
import interface
import to_html

cookie_secret = 'IUASDFN'



app = bottle.Bottle()
@app.error(404)
def error404(error):
	return 'Page not found.'


@app.route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root='static')

@app.route('/images/<filename>')
def server_images(filename):
	return static_file(filename, root='images')





@app.route('/')
def main():
	#check cookies for user logged in
	error = get_cookie('error')
	if not error:
		error = ''
	set_cookie('error','')
	username = get_cookie('username')

	if username:
		user = insta.User(username)
		#update photo queue
		photo_queue = interface.get_photo_queue(username)

		
		photo_queue_html = to_html.photo_queue(photo_queue)


		#get current photo
		current_image = interface.get_current_photo(username)
		
		current_image_html = to_html.current_image(current_image)



		return bottle.template(os.path.join('templates','index.tpl'),
			username=username,
			profile_picture=user.get_profile_picture(),
			current_image_html=current_image_html,
			photo_queue_html=photo_queue_html
			)

	#return home page with logged out view
	post, image = insta.get_random_image()
	image_url = f'https://www.instagram.com/p/{post}'

	set_cookie('auth_image_url',image_url)
	

	return bottle.template(os.path.join('templates','login.tpl'),
		image_url=image_url,
		image=image,
		error=error)


#select a photo to upload 
@app.post('/choose_new')
def choose_new():
	username = get_cookie('username')
	if not username:
		bottle.redirect('/')

	user = insta.User(username)

	current_image = interface.get_current_photo(username)

	recent_photos, recent_photos_urls = user.get_recent(current_image)

	images_html = to_html.select_photo(recent_photos)

	return bottle.template(os.path.join('templates','choose.tpl'),
		username=username,
		profile_picture = user.get_profile_picture(),
		images_html=images_html,
		recent_photos_urls=recent_photos_urls,
		recent_photos=recent_photos
		)



@app.post('/login')
def login():
	#check credentials
	username = bottle.request.forms['username']
	raw_password = bottle.request.forms['password']
	#encrypt password
	
	valid = interface.check_credentials(username, raw_password)
	if valid:
		set_cookie('username',username)
	else:
		set_cookie('error','Either username or password is incorrect.')
	bottle.redirect('/')

	

@app.post('/logout')
def logout():
	set_cookie('username','')
	bottle.redirect('/')


@app.post('/create')
def create_account():

	#check username valid
	#check password valid
	username = bottle.request.forms['username']
	raw_password1 = bottle.request.forms['password1']
	raw_password2 = bottle.request.forms['password2']

	valid_username = interface.check_valid_username(username)
	valid_password = interface.check_valid_password(raw_password1, raw_password2)

	if not valid_username:
		set_cookie('error', 'That username is taken.')
		bottle.redirect('/')

	if not valid_password:
		set_cookie('error', 'That password is invalid.')
		bottle.redirect('/')

	#check account is authentic
	#check user has commented on photo
	#--get photo url from cookie
	#--check comments
	valid_account = insta.check_valid_account(username, get_cookie('auth_image_url'))

	if valid_account:
		#encrypt pass
		password = security.encrypt_password(raw_password1)
		#creat accounte
		interface.create_account(username, password)
		#login
		set_cookie('username',username)
	else:
		set_cookie('error', 'Please comment on the photo before attempting to validate account.')


	bottle.redirect('/')




@app.post('/upload')
def upload():
	image_id, image_url = bottle.request.forms['image_url'].split('?SPLIT?')
	#add image to db
	username = get_cookie('username')
	interface.add_photo_to_database(username, image_id, image_url)
	interface.update_current_photo(username, image_id)
	bottle.redirect('/')


	



def set_cookie(cookie_name, cookie_value):
	bottle.response.set_cookie(cookie_name, cookie_value, secret = cookie_secret)

def get_cookie(cookie_name):
	try:
		return bottle.request.get_cookie(cookie_name, secret=cookie_secret)
	except:
		return None




if __name__ == "__main__":
	app.run()