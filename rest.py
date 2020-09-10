import dao
from app import app
from flask import jsonify, request, session
		
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

	_username = _json['username']
	_password = _json['password']
	_name = _json['name']
	
	if _username and _password and _name:
		user = dao.signup(_name, _username, _password)
		
		if user != None:
			session['username'] = user
			return jsonify({'message' : 'User successfully created'})

	resp = jsonify({'message' : 'Bad Request - email already being used'})
	resp.status_code = 400
	return resp