import pymysql
from db_config import mysql
from mail_config import mail
from werkzeug.security import check_password_hash
			
def login(email, pwd):
	conn = None;
	cursor = None;
	
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		
		sql = "SELECT email, pwd FROM users WHERE email=%s"
		sql_where = (email,)
		
		cursor.execute(sql, sql_where)
		row = cursor.fetchone()

		if row:
			if (row[1] == pwd):
				return row[0]
		return None

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()

def signup(firstname, lastname, email, pwd):
	conn = None;
	cursor = None;
	
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
        
		sql = "SELECT email, firstname  FROM users WHERE email=%s"
		sql_where = (email,)
		
		cursor.execute(sql, sql_where)
		row = cursor.fetchone()
		if (row == None):
			sql = "INSERT  INTO users(firstname, lastname, email, pwd) VALUES (%s, %s, %s, %s)"
			val = (firstname, lastname, email, pwd);
			cursor.execute(sql, val)
			conn.commit()
			return email
		return None            
        
	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()
            
def contact(name, email, message):
	conn = None;
	cursor = None;
	
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
        
		if (name and email and message):
			sql = "INSERT  INTO emails(name, email, message) VALUES (%s, %s, %s)"
			val = (name, email, message);
			cursor.execute(sql, val)
			conn.commit()
			return email
		return None            
        
	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()