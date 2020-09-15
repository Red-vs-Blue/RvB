from app import app
from flask_mail import Mail, Message

mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ''       # Type in your gmail account in here. This is the account that will send out and receive the emails.
app.config['MAIL_PASSWORD'] = ''                            # Type in your gmail password in here
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)