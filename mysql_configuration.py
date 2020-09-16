import mysql.connector

# Change the credentials accordingly
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

# Creating a database
# mycursor.execute("CREATE DATABASE mydatabase")

# Print out all databases
# mycursor.execute("SHOW DATABASES")
#for x in mycursor:
#  print(x)

# Create an user table with two attributes such as name and email
#mycursor.execute("CREATE TABLE users (firstname varchar(50) NULL, lastname varchar(50) NULL, email varchar(50) NULL, pwd varchar(255) NULL, admin tinyint DEFAULT 0, id int unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY)")
#mydb.commit()

#mycursor.execute("CREATE TABLE emails (name varchar(50) NULL, email varchar(50) NULL, message varchar(1000) NULL)")
#mydb.commit()

#Print out all the tables in the database
#mycursor.execute("SELECT * FROM users")

#Dropping the user table
#mycursor.execute("DROP TABLE users")

#for x in mycursor:
#  print(x) 



def insert_user(firstname, lastname, email, pwd):
    sql = "Insert  into users(firstname, lastname, email, pwd) VALUES (%s, %s, %s, %s)"
    val = (firstname, lastname, email, pwd);
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

# Inserting a test user
#insert_user("Hussain", "Al Zerjawi", "tester@gmail.com", "Password123");

#mydb.commit()
#mycursor.execute("SELECT * FROM users;")
#mydb.commit()

