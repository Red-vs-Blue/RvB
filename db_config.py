from app import application
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
# Your MySQL Database username
application.config['MYSQL_DATABASE_USER'] = 'root'
# Be sure to add your MySQL server's password here
application.config['MYSQL_DATABASE_PASSWORD'] = ''
# The name of your database
application.config['MYSQL_DATABASE_DB'] = ''
# Where your server is running
application.config['MYSQL_DATABASE_HOST'] = ''

mysql.init_app(application)
