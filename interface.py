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

	sql = f'''
	INSERT INTO photos VALUES ("{image_id}", "{username}", "{image_url}", 0,0,0);
	'''

	curr.execute(sql)
	db.commit()



def get_current_photo(username):
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


	






	


