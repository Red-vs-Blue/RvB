import rest
from app import application
from flask import render_template

@application.route('/')
def home_page():
	return render_template('index.html')

@application.route('/about/page')
def about_page():
	return render_template('about.html')

@application.route('/contact/page')
def contact_page():
	return render_template('contact.html')
	
@application.route('/issues/page')
def issues_page():
	return render_template('issues.html')

@application.route('/local/page')
def local_page():
	return render_template('local.html')
    
@application.route('/login/page')
def login_page():
	return render_template('login.html')

@application.route('/politicians/page')
def politicians_page():
	return render_template('politicians.html')

@application.route('/signup/page')
def signup_page():
	return render_template('signup.html')

@application.route('/faq/page')
def faq_page():
	return render_template('faq.html')

@application.route('/user_profile/page')
def user_profile_page():
	return render_template('user_profile.html')
		
if __name__ == "__main__":
	application.debug = True
	application.run(port = 8000)