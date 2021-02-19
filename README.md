# Welcome to Red vs Blue!

Click here to visit the site: http://elephantdonkey-env.eba-rbzqkb4y.us-east-1.elasticbeanstalk.com

This README will guide you through our Web development.
# Before you start:

## You need to have these requirements before starting with our repo:
You need to have Python working on your system. We recommend using the latest version of Python 3. Flask supports Python 3.5 and newer, Python 2.7. Furthermore, you need a working MySQL server with the version 8.0.1.8. Additionally, once you have the credentials for your MySQL server, you need to include this information into the db_config.py file so that the Python application can connect and alter the database. Furthermore the database currently does not have any tables nor any attributes. By adapting and using the mysql_configuration.py file, you can change your database structure. Besides the MySQL server needing to be properly configured so does the mail credentials to be configured. To do this the mail_config.py file needs to be changed accordingly to your gmail account. 
## How to use our website.

### Through the "venv" virtual environment in python.
- Firstly, create a clone of our repository on your local machine.
- Go to the root directory of the repository in your terminal.
- To activate the virtual environment:
	- If you are using UNIX or MacOS then type in:
		- venv/bin/activate
	- If you are using Windows then type in:
		- venv/Scripts/activate
- Once you have the virtual environment running, you don't need to be concerned about installing any other libraries as all the required libraries are already installed on the virtual environment.
- To run the website type in the following command into the terminal:
	- python main.py
- The terminal should output a localhost address such as:
	- http://127.0.0.1:5000/
- Go onto that localhost on your web browser. Now you should be able to view and interact with the website.

### Through the "requirement.txt"
- Firstly, create a clone of our repository on your local machine.
- Go to the root directory of the repository in your terminal.
- Type the following into your terminal to install all the necessary libraries.
	- pip install -r requirements.txt
- If this doesn't work due to pip not being included in your PATH then type in:
	- python -m pip install -r requirements.txt
- Once this is done you can run:
	- python main.py
- The terminal should output a localhost address such as:
	- http://127.0.0.1:5000/
- Go onto that localhost on your web browser. Now you should be able to view and interact with the website.
