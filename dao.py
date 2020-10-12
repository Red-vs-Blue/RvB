import pymysql
import datetime
from db_config import mysql
from mail_config import mail
from werkzeug.security import check_password_hash


def login(email, pwd):
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor()

        sql = "SELECT username, first, last, email, party, password, creation_date FROM accounts WHERE email=%s"
        sql_where = (email,)

        cursor.execute(sql, sql_where)
        row = cursor.fetchone()

        if row:
            if (row[5] == pwd):
                return row
        return None

    except Exception as e:
        print(e)

    finally:
        if cursor and conn:
            cursor.close()
            conn.close()


def signup(username, firstname, lastname, email, party, pwd):
    conn = None
    cursor = None
    creation_date = datetime.datetime.now()
    try:
        conn = mysql.connect()
        cursor = conn.cursor()

        sql = "SELECT email, first  FROM accounts WHERE email=%s"
        sql_where = (email,)

        cursor.execute(sql, sql_where)
        row = cursor.fetchone()
        if (row == None):
            sql = "INSERT  INTO accounts(username, first, last, email, party, password, creation_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            # Create a specific function call for turning party string into int
            if (party == "Democrat" or party == "democrat"):
                party = 2
            else:
                party = 1
            val = (username, firstname, lastname, email, party, pwd, creation_date)
            cursor.execute(sql, val)
            conn.commit()
            return username
        return None

    except Exception as e:
        print(e)

    finally:
        if cursor and conn:
            cursor.close()
            conn.close()


def contact(name, email, message):
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor()

        if (name and email and message):
            sql = "INSERT  INTO emails(name, email, message) VALUES (%s, %s, %s)"
            val = (name, email, message)
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
            
def retrieve_thread():
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        
        sql = "SELECT username, affiliation, post_text, time_and_date, votes, page, post_title  FROM posts"

        cursor.execute(sql)
        row = cursor.fetchone()
        return row


    except Exception as e:
        print(e)

    finally:
        if cursor and conn:
            cursor.close()
            conn.close()

def pageID_to_page(pageID):
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        
        sql = "SELECT id, title, area, votes  FROM pages WHERE id=%s"
        sql_where = ( int(pageID))

        cursor.execute(sql, sql_where)

        row = cursor.fetchone()
        return row[1]


    except Exception as e:
        print(e)

    finally:
        if cursor and conn:
            cursor.close()
            conn.close()

def partyID_to_party(partyID):
    conn = None
    cursor = None

    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        
        sql = "SELECT id, affiliation FROM affiliation WHERE id=%s"
        sql_where = ( int(partyID))

        cursor.execute(sql, sql_where)

        row = cursor.fetchone()
        return row[1]


    except Exception as e:
        print(e)

    finally:
        if cursor and conn:
            cursor.close()
            conn.close()