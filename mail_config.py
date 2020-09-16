from app import application
from flask_mail import Mail, Message

mail = Mail(application)

application.config['MAIL_SERVER']='smtp.gmail.com'
application.config['MAIL_PORT'] = 465
application.config['MAIL_USERNAME'] = ''       # Type in your gmail account in here. This is the account that will send out and receive the emails.
application.config['MAIL_PASSWORD'] = ''                            # Type in your gmail password in here
application.config['MAIL_USE_TLS'] = False
application.config['MAIL_USE_SSL'] = True

mail = Mail(application)