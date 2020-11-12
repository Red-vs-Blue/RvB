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
            session['party'] = dao.partyID_to_party(user[4])
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
        postdict = {

        }
        postdict['post_username'] = thread[0]
        postdict['post_affiliation'] = dao.partyID_to_party(thread[1])
        postdict['post_text'] = thread[2]
        postdict['time_and_date'] = thread[3]
        postdict['post_votes'] = thread[4]
        postdict['page'] = dao.pageID_to_page(thread[5])
        postdict['post_title'] = thread[6]
        postdict['post_id'] = thread[7]
        return postdict
        #return jsonify({'message': 'Thread successfully retrieved'})

@application.route('/update_password', methods=['POST'])
def update_password():
    _json = request.json
    _newPassword = _json['newPassword']
    _confirmPassword = _json['confirmPassword']
    update = dao.change_password(_newPassword, session['username'])
    if update == True:
        return jsonify({'message': 'User successfully updated'})
        
@application.route('/upvote', methods=['POST'])
def upvote():
    _json = request.json
    _email = _json['email']
    _post_id = _json['post_id']
    upvoteStatus = dao.upvote(_email, _post_id)
    if upvoteStatus == True:
        return jsonify({'message': 'Upvote was successful'})
    else:
        resp = jsonify({'message': 'You have already upvoted'})
        resp.status_code = 400
        return resp

@application.route('/downvote', methods=['POST'])
def downvote():
    _json = request.json
    _email = _json['email']
    _post_id = _json['post_id']
    downvoteStatus = dao.downvote(_email, _post_id)
    if downvoteStatus == True:
        return jsonify({'message': 'Downvote was successful'})
    else:
        resp = jsonify({'message': 'You have already downvoted'})
        resp.status_code = 400
        return resp

@application.route('/star', methods=['POST'])
def star():
    _json = request.json
    _email = _json['email']
    _post_id = _json['post_id']
    starStatus = dao.star(_email, _post_id)
    if starStatus == True:
        return jsonify({'message': 'Bookmark was successful'})
    else:
        return jsonify({'message': 'You have unmarked this post.'})

@application.route('/checkVoteStatus', methods=['POST'])
def checkVoteStatus():
    _json = request.json
    _email = _json['email']
    _post_id = _json['post_id']
    voteStatus = dao.checkVoteStatus(_email, _post_id)
    return voteStatus