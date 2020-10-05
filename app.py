from flask import Flask

application = Flask(__name__, template_folder='static/html')
application.secret_key = "secret key"
