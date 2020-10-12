import dao
import datetime
from app import application
from flask import jsonify, request, session, redirect, url_for
from mail_config import mail
from flask_mail import Mail, Message


@application.route('/login', methods=['POST'])
def login():
    _json = request.json

    _email = _json['email']
    _password = _json['password']

    if _email and _password:
        user = dao.login(_email, _password)

        if user != None:
            session['username'] = user[0]
            session['first'] = user[1]
            session['last'] = user[2]
            session['email'] = user[3]
            session['party'] = user[4]
            session['date'] = user[6]
            return jsonify({'message': 'User logged in successfully'})

    resp = jsonify({'message': 'Bad Request - invalid credentials'})
    resp.status_code = 400
    return resp


@application.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
        session.pop('first', None)
        session.pop('last', None)
        session.pop('email', None)
        session.pop('party', None)
        session.pop('date', None)
    #return (redirect(url_for('.home_page')))
    return jsonify({'message': 'You successfully logged out'})


@application.route('/signup', methods=['POST'])
def signup():
    _json = request.json

    _username = _json['username']
    _firstname = _json['first']
    _lastname = _json['last']
    _email = _json['email']
    _party = _json['party']
    _password = _json['password']

    if _username and _password and _firstname and _lastname and _email and _party:
        user = dao.signup(_username, _firstname, _lastname, _email, _party, _password)

        if user != None:
            session['username'] = user
            session['first'] = _firstname
            session['last'] = _lastname
            session['email'] = _email
            session['party'] = _party
            session['date'] = datetime.datetime.now()
            return jsonify({'message': 'User successfully created'})

    resp = jsonify({'message': 'Bad Request - email already being used'})
    resp.status_code = 400
    return resp


@application.route('/contact', methods=['POST'])
def contact():
    _json = request.json

    _name = _json['name']
    _email = _json['email']
    _message = _json['message']
    if _name and _email and _message:
        msg = Message('The subject', sender=_email, recipients=[
                      'contactelephantdonkey@gmail.com'])
        msg.body = "Name: " + _name + "\n" + "From: " + \
            _email + "\n" + "Message: " + _message
        mail.send(msg)
        email_message = dao.contact(_name, _email, _message)

        if email_message != None:
            return jsonify({'message': 'Email successfully sent.'})

    resp = jsonify({'message': 'Bad Request - invalid credendtials'})
    resp.status_code = 400
    return resp

@application.route('/retrieve_thread', methods=['GET'])
def retrieve_thread():
    thread = dao.retrieve_thread()
    
    if thread != None:
        #p1 = post(thread[0], thread[1], thread[2], thread[3], thread[4], thread[5], thread[6])
        session['post_username'] = thread[0]
        session['post_affiliation'] = dao.partyID_to_party(thread[1])
        session['post_text'] = thread[2]
        session['time_and_date'] = thread[3]
        session['post_votes'] = thread[4]
        session['page'] = dao.pageID_to_page(thread[5])
        session['post_title'] = thread[6]
        return jsonify({'message': 'Thread successfully retrieved'})

class post:
  def __init__(self, username, affiliation, post_text, time_and_date, votes, page, post_title):
    self.username = username
    self.affiliation = affiliation
    self.post_text = post_text
    self.time_and_date = time_and_date
    self.votes = votes
    self.page = page
    self.post_title = post_title 