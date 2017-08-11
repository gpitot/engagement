import sqlite3

sqlite_file = 'engageDB.db'
conn = sqlite3.connect(sqlite_file)

c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON")
print(c.execute("PRAGMA foreign_keys"))


def add_user_table():
	sql = '''
	DROP TABLE IF EXISTS users;
	CREATE TABLE users (
	           userID text unique primary key,
	           password text,
	           doc text, 
	           rating number,
	           photoID text,
	           FOREIGN KEY(photoID) REFERENCES photos(photoID)

	           
	);'''

	c.executescript(sql)
	conn.commit()


def add_photo_table():
	sql = '''
	DROP TABLE IF EXISTS photos;
	CREATE TABLE photos (
	           photoID text unique primary key,
	           userID text,
	           photo_url text,
	           likes_owed number,
	           likes_recieved number,
	           skips_recieved number,
	           FOREIGN KEY(userID) REFERENCES users(userID)

	           
	);'''

	c.executescript(sql)
	conn.commit()

def insert_dummy_data():
	sql = '''
	INSERT INTO photos VALUES ('photo1','user1',  0,0,0);
	'''
	c.executescript(sql)
	conn.commit()



add_user_table()
#insert_dummy_data()

add_photo_table()



