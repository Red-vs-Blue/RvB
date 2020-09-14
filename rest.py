import dao
from app import app
from flask import jsonify, request, session
from mail_config import mail
from flask_mail import Mail, Message
		
@app.route('/login', methods=['POST'])
def login():
	_json = request.json

	_username = _json['username']
	_password = _json['password']
	
	if _username and _password:
		user = dao.login(_username, _password)
		
		if user != None:
			session['username'] = user
			return jsonify({'message' : 'User logged in successfully'})

	resp = jsonify({'message' : 'Bad Request - invalid credendtials'})
	resp.status_code = 400
	return resp

@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username', None)
	return jsonify({'message' : 'You successfully logged out'})
    
@app.route('/signup', methods=['POST'])
def signup():
	_json = request.json
	print(_json)
    
	_firstname = _json['first']
	_lastname = _json['last']
	_username = _json['username']
	_password = _json['password']
    
	
	if _username and _password and _firstname and _lastname:
		user = dao.signup(_firstname, _lastname, _username, _password)
		
		if user != None:
			session['username'] = user
			return jsonify({'message' : 'User successfully created'})

	resp = jsonify({'message' : 'Bad Request - email already being used'})
	resp.status_code = 400
	return resp
    
@app.route('/contact', methods=['POST'])
def contact():
	_json = request.json

	_name = _json['name']
	_email = _json['email']
	_message = _json['message']
	if _name and _email and _message:
		msg = Message('The subject', sender = _email, recipients = ['contactelephantdonkey@gmail.com'])
		msg.body = "Name: " + _name + "\n" + "From: " + _email + "\n" + "Message: " + _message
		mail.send(msg)
		email_message = dao.contact(_name, _email, _message)
		
		if email_message != None:
			return jsonify({'message' : 'Email successfully sent.'})

	resp = jsonify({'message' : 'Bad Request - invalid credendtials'})
	resp.status_code = 400
	return resp