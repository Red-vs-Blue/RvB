from app import application
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
# Your MySQL Database username
application.config['MYSQL_DATABASE_USER'] = 'admin'
# Be sure to add your MySQL server's password here
application.config['MYSQL_DATABASE_PASSWORD'] = 'Bernie2020'
# The name of your database
application.config['MYSQL_DATABASE_DB'] = 'RvB'
# Where your server is running
application.config['MYSQL_DATABASE_HOST'] = 'rvbdb.csw5x1n7bdpk.us-east-1.rds.amazonaws.com'

mysql.init_app(application)
