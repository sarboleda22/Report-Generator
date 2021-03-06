import requests
from flask import render_template, url_for, request, redirect, jsonify, make_response
from flask_restful import Resource
from app import app, db, api
from models import Slide


class RestSlides(Resource):
	#Handles the GET requests
	def get(self):
			response = {}
			response['count'] = Slide.query.count() #Creates an item in the dict. with key 'count' and value <the number of rows in the database>
			response['results'] = []	#creates another item in the dict w key 'results' and an empty list as the value
			slides = Slide.query.all()	#the set of slides for iterating later
			for i in slides:
				results = {}
				results['name'] = i.name
				results['object_id'] = i.object_id
				response['results'].append(results)
			return response
	#Handles the POST requests
	def post(self):
		#Use table 'slides'
		__tablename__ = 'slides'

		name = request.form['name']
		content = request.form['content']
		new_slide = Slide(name, content)
		db.session.add(new_slide)
		db.session.commit()
		return 'New Slide Created | name : {} | content : {}'.format(name, content)

class DeleteSlide(Resource):
	def delete(self, object_id):
		a = Slide.query.get(object_id) #Search for object in the database with id:object_id
		del_name = a.name
		del_id = a.object_id
		db.session.delete(a) #Deleted the object
		db.session.commit() #Commit the deletion
		return 'Slide {} with ID {} has been successfuly deleted'.format(del_name, del_id)

#RENDERING SLIDES
@app.route('/slides/<object_id>/', methods=['GET'])
def presentation(object_id):
	obj = Slide.query.get(object_id)
	content = obj.content
	return render_template('main.html', content=content)


#Run the API in .../slides/
api.add_resource(RestSlides, '/slides/')
api.add_resource(DeleteSlide, '/slides/<object_id>/')