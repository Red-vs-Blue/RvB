import pymysql
import datetime
from flask import jsonify
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
            elif (party == "Liberterian" or party == "liberterian"):
                party = 3
            elif (party == "Green" or party == "green"):
                party = 4
            elif (party == "Constitution" or party == "constitution"):
                party = 5
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
        
        sql = "SELECT username, affiliation, post_text, time_and_date, votes, page, post_title, id  FROM posts"

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
            
def change_password(password, username):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "UPDATE accounts SET password=%s WHERE username=%s"
        sql_where = (password, username)
        cursor.execute(sql, sql_where)
        conn.commit()
        return True


    except Exception as e:
        print(e)

    finally:
        if cursor and conn:
            cursor.close()
            conn.close()
            
def upvote(email, post_id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        # Check first whether a vote was already made
        sql = "SELECT voteStatus FROM postVotes WHERE post_id=%s AND email=%s"
        sql_where = (int(post_id), email)
        cursor.execute(sql, sql_where)
        row = cursor.fetchone()
        if row is None:
            sql = "INSERT  INTO postVotes(post_id, voteStatus, email) VALUES (%s, %s, %s)"
            val = (int(post_id), 1, email)
            cursor.execute(sql, val)
            conn.commit()
            #Increment the votes attribute in the post table of the database
            sql = "UPDATE posts SET votes=votes + 1 WHERE id=%s"
            sql_where = (int(post_id))
            cursor.execute(sql, sql_where)
            conn.commit()
            return True
        elif row[0] == 1:
            #Do nothing since the post has already been upvoted
            return False
        elif row[0] == 2:       
            sql = "UPDATE postVotes SET voteStatus=1 WHERE post_id=%s AND email=%s"
            sql_where = (int(post_id), email)
            cursor.execute(sql, sql_where)
            conn.commit()
            
            sql = "UPDATE posts SET votes=votes + 2 WHERE id=%s"
            sql_where = (int(post_id))
            cursor.execute(sql, sql_where)
            conn.commit()
            return True


    except Exception as e:
        print(e)

    finally:
        if cursor and conn:
            cursor.close()
            conn.close()

def downvote(email, post_id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        # Check first whether a vote was already made
        sql = "SELECT voteStatus FROM postVotes WHERE post_id=%s AND email=%s"
        sql_where = (int(post_id), email)
        cursor.execute(sql, sql_where)
        row = cursor.fetchone()
        if row is None:
            sql = "INSERT  INTO postVotes(post_id, voteStatus, email) VALUES (%s, %s, %s)"
            val = (int(post_id), 2, email)
            cursor.execute(sql, val)
            conn.commit()
            #Increment the votes attribute in the post table of the database
            sql = "UPDATE posts SET votes=votes + 1 WHERE id=%s"
            sql_where = (int(post_id))
            cursor.execute(sql, sql_where)
            conn.commit()
            return True
        elif row[0] == 1:
            sql = "UPDATE postVotes SET voteStatus=2 WHERE post_id=%s AND email=%s"
            sql_where = (int(post_id), email)
            cursor.execute(sql, sql_where)
            conn.commit()
            
            sql = "UPDATE posts SET votes=votes - 2 WHERE id=%s"
            sql_where = (int(post_id))
            cursor.execute(sql, sql_where)
            conn.commit()
            return True
        elif row[0] == 2: 
            #Do nothing since the post has already been upvoted
            return False        



    except Exception as e:
        print(e)

    finally:
        if cursor and conn:
            cursor.close()
            conn.close()

def star(email, post_id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        # Check first whether a vote was already made
        sql = "SELECT id, bookmarkStatus FROM postVotes WHERE post_id=%s AND email=%s"
        sql_where = (int(post_id), email)
        cursor.execute(sql, sql_where)
        row = cursor.fetchone()
        if row is None:
            sql = "INSERT  INTO postVotes(post_id, bookmarkStatus, email) VALUES (%s, %s, %s)"
            val = (int(post_id), 1, email)
            cursor.execute(sql, val)
            conn.commit()
            return True
        elif row[1] == 1:
            sql = "UPDATE postVotes SET bookmarkStatus=0 WHERE post_id=%s AND email=%s"
            sql_where = (int(post_id), email)
            cursor.execute(sql, sql_where)
            conn.commit()
            return False
        elif row[1] == 0: 
            sql = "UPDATE postVotes SET bookmarkStatus=1 WHERE post_id=%s AND email=%s"
            sql_where = (int(post_id), email)
            cursor.execute(sql, sql_where)
            conn.commit()
            return True       



    except Exception as e:
        print(e)

    finally:
        if cursor and conn:
            cursor.close()
            conn.close()
            
def checkVoteStatus(email, post_id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        # Check first whether a vote was already made
        sql = "SELECT id, voteStatus, bookmarkStatus FROM postVotes WHERE post_id=%s AND email=%s"
        sql_where = (int(post_id), email)
        cursor.execute(sql, sql_where)
        row = cursor.fetchone()
        if row is None:
            return jsonify({'voteStatus': 0, 'bookmarkStatus': 0})
        else:
            return jsonify({'voteStatus': row[1], 'bookmarkStatus': row[2]})



    except Exception as e:
        print(e)

    finally:
        if cursor and conn:
            cursor.close()
            conn.close()