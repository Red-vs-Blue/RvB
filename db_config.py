from app import application
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
application.config['MYSQL_DATABASE_USER'] = 'root'              # Your MySQL Database username
application.config['MYSQL_DATABASE_PASSWORD'] = ''              # Be sure to add your MySQL server's password here
application.config['MYSQL_DATABASE_DB'] = ''          # The name of your database
application.config['MYSQL_DATABASE_HOST'] = ''         # Where your server is running

mysql.init_app(application)