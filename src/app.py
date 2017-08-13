from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

#App initialized in Flask
app = Flask(__name__)
api = Api(app)

#Setting the track of modifications off
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#User info of the database, in this case, postgres
db_info = {
	'username':'hacknoob',
	'password':'qwerty1234',
	'host':'localhost',
	'db_name':'prueba',
}

#Defining the URI of the db with the info given before. In this example, it is running on a localhost
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}/{}'.format(db_info['username'], db_info['password'], db_info['host'], db_info['db_name'])

#Initializing the db object
db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
	db.create_all()
	#DEBUG MUST BE FALSE BEFORE DEPLOYMENT
	app.run(debug=True)