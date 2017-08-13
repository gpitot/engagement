#all db related functions like login
import sqlite3
import security

def connect():
    conn = sqlite3.connect('engageDB.db')
    return conn


def check_credentials(username, raw_password):
	#check credentials on db
	db = connect()
	curr = db.cursor()

	sql = f'''
	SELECT * FROM users WHERE userID = "{username}";'''
	curr.execute(sql)
	result = curr.fetchall()

	
	for r in result:
		
		return security.verify_password(raw_password, r[1])

	return False



def check_valid_username(username):

	if len(username) > 0:
		db = connect()
		curr = db.cursor()

		sql = f'''
		SELECT userID FROM users WHERE userID = "{username}";
		'''
		curr.execute(sql)
		result = curr.fetchall()

		if len(result) < 1:
			return True
	#check if username is in use or not
	return False


def check_valid_password(raw_password, raw_password2):
	if len(raw_password) > 0 and raw_password == raw_password2:
		return True
	return False



def create_account(username, password):
	db = connect()
	curr = db.cursor()

	sql = f'''
	INSERT INTO users VALUES ("{username}", "{password}",  datetime('now'), 0, Null);
	'''
	curr.execute(sql)
	db.commit()



def add_photo_to_database(username, image_id, image_url):
	db = connect()
	curr = db.cursor()

	print("check photo in db ", check_if_photo_in_db(image_id))
	if check_if_photo_in_db(image_id):
		print('returning...')
		return



	sql = f'''
	INSERT INTO photos VALUES ("{image_id}", "{username}", "{image_url}", 3,0,0);
	'''

	curr.execute(sql)
	db.commit()

def check_if_photo_in_db(image_id):
	db = connect()
	curr = db.cursor()

	sql = f'''
	SELECT photoID FROM photos WHERE photoID = "{image_id}";
	'''
	curr.execute(sql)
	res = curr.fetchall()
	return len(res) > 0


def get_current_photo_url(username):
	db = connect()
	curr = db.cursor()

	sql = f'''
	SELECT photoID FROM users WHERE userID = "{username}";
	'''
	curr.execute(sql)
	res = curr.fetchall()
	if res:
		for r in res:
			photo_id = r[0]

		sql = f'''
		SELECT photo_url FROM photos WHERE photoID = "{photo_id}";
		'''
		curr.execute(sql)
		res = curr.fetchall()
		for r in res:
			return r[0]

	return None


def update_current_photo(username, image_id):
	db = connect()
	curr = db.cursor()

	sql = f'''
	UPDATE users SET photoID = "{image_id}" WHERE userID = "{username}";
	'''
	curr.execute(sql)
	db.commit()





#get photo queue
def get_photo_queue(username):
	#order users by rating - 
	#get current photo
	#append to list
	#THEN 

	#use list to get photo information from photos
	#if lieks recieved < likes owed then append to list
	#photo id photo url 

	photo_queue = []

	db = connect()
	curr = db.cursor()


	#get list of photos user has engaged already
	sql = f'SELECT photoID FROM user_engagement WHERE userID = "{username}";'
	curr.execute(sql)
	engaged_on = [x[0] for x in curr.fetchall()]


	sql = f'''
	SELECT photoID FROM users WHERE userID != "{username}" ORDER BY rating;
	'''
	curr.execute(sql)
	res = curr.fetchall()
	
	for r in res:
		sql = f'SELECT photoID, photo_url, likes_owed, likes_recieved FROM photos WHERE photoID = "{r[0]}";'
		curr.execute(sql)
		photo_info = curr.fetchall()
		
		
		if photo_info[0][2] > photo_info[0][3] and photo_info[0][0] not in engaged_on:
			photo_queue.append((photo_info[0][0], photo_info[0][1]))




	return photo_queue







def update_engagement(username, photoID):
	#update likesrecieved
	update_likes_recieved_AND_owed(photoID, 'likes_recieved')
	#update likes_owed
	update_likes_recieved_AND_owed(get_photoID(username), 'likes_owed')
	#update likes_given
	update_likes_given(username, photoID)
	return






def update_likes_recieved_AND_owed(photoID, operation):
	db = connect()
	curr = db.cursor()

	sql = f'SELECT {operation} FROM photos WHERE photoID = "{photoID}";'
	curr.execute(sql)
	res = curr.fetchall()
	like_count = res[0][0]

	sql = f'''
	UPDATE photos SET {operation} = {like_count+1} WHERE photoID = "{photoID}";
	'''
	curr.execute(sql)
	db.commit()


def get_photoID(username):
	#get current photo then update likes
	db = connect()
	curr = db.cursor()

	sql = f'''
	SELECT photoID FROM users WHERE userID = "{username}";
	'''
	curr.execute(sql)
	res = curr.fetchall()
	

	return res[0][0]


def update_likes_given(username, photoID):
	#in new table
	#update likes given
	db = connect()
	curr = db.cursor()
	sql = f'''
	INSERT INTO user_engagement VALUES ("{username}", "{photoID}");
	'''
	curr.execute(sql)
	db.commit()

	



