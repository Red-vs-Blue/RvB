import pymysql
from db_config import mysql
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

def signup(name, email, pwd):
	conn = None;
	cursor = None;
	
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
        
		sql = "SELECT email, name  FROM users WHERE email=%s"
		sql_where = (email,)
		
		cursor.execute(sql, sql_where)
		row = cursor.fetchone()
		if (row == None):
			sql = "INSERT  INTO users(name, email, pwd) VALUES (%s, %s, %s)"
			val = (name, email, pwd);
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