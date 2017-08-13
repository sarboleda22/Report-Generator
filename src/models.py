"""
File used for defining all the models of the app
"""
from app import db

class Slide(db.Model):
	object_id = db.Column(db.Integer, primary_key=True) #May need to add UUID for increased security
	name = db.Column(db.String(80))
	content = db.Column(db.Text)

	def __init__(self, name, content):
		self.name = name
		self.content = content

	def __repr__(self):
		return '<ID {} | User {}>'.format(str(self.object_id), self.name)

