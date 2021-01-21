from app import application
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
# Your MySQL Database username
application.config['MYSQL_DATABASE_USER'] = 'admin'
# Be sure to add your MySQL server's password here
application.config['MYSQL_DATABASE_PASSWORD'] = 'akld3fnni5pen7iwwi'
# The name of your database
application.config['MYSQL_DATABASE_DB'] = 'RvBdatabase' #change name in code too
# Where your server is running
application.config['MYSQL_DATABASE_HOST'] = 'rvbdatabase.c7we0ng6fgli.us-east-2.rds.amazonaws.com'

mysql.init_app(application)
