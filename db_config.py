from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'              # Your MySQL Database username
app.config['MYSQL_DATABASE_PASSWORD'] = ''              # Be sure to add your MySQL server's password here
app.config['MYSQL_DATABASE_DB'] = 'mydatabase'          # The name of your database
app.config['MYSQL_DATABASE_HOST'] = 'localhost'         # Where your server is running
mysql.init_app(app)