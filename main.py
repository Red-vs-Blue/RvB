import rest
from app import app
from flask import render_template

@app.route('/')
def home_page():
	return render_template('index.html')

@app.route('/about/page')
def about_page():
	return render_template('about.html')

@app.route('/contact/page')
def contact_page():
	return render_template('contact.html')
	
@app.route('/issues/page')
def issues_page():
	return render_template('issues.html')

@app.route('/local/page')
def local_page():
	return render_template('local.html')
    
@app.route('/login/page')
def login_page():
	return render_template('login.html')

@app.route('/politicians/page')
def politicians_page():
	return render_template('politicians.html')

@app.route('/signup/page')
def signup_page():
	return render_template('signup.html')
		
if __name__ == "__main__":
    app.run()