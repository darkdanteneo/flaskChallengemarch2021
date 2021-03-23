"""Routes for the course resource.
"""

from run import app, Course, db
from flask import request, jsonify, make_response
from http import HTTPStatus
import json
from datetime import datetime
from sqlalchemy import or_, exists


@app.route("/course/<int:id>", methods=['GET'])
def get_course(id):
    if request.method == 'GET':
        exist = db.session.query(exists().where(Course.id == id)).scalar()
        if not exist:
            return jsonify({"messge": "Course "+str(id)+" does not exist"})
        course = Course.query.get(id)
        return make_response(jsonify({"data": course.serialize() }), 200)

@app.route("/course", methods=['GET'])
def get_courses():

    if request.method == 'GET':
        pageNumber = 1
        pageSize = 10
        titleWords = ""
        words = []
        if 'page-number' in request.args:
                pageNumber = int(request.args.get('page-number'))
        if 'page-size' in request.args:
                pageSize = int(request.args.get('page-size'))
        if 'title-words' in request.args:
            titleWords = request.args.get('title-words')
            words = titleWords.split(",")
        courses = Course.query.filter(or_(Course.title.contains(word) for word in words))[(pageNumber-1)*pageSize:(pageNumber)*pageSize]
        return make_response(jsonify({"data": [course.serialize() for course in courses]}), 200)


@app.route("/course", methods=['POST'])
def create_course():
    # Bonus points for validating the POST body fields
    if request.method =='POST':
        content =request.get_json()
        description = content['description']
        image_path = content['image_path']
        on_discount = content['on_discount']
        price = content['price']
        title = content['title']
        new_task  = Course(description=description, image_path=image_path, on_discount=on_discount, price=price, title=title)
        db.session.add(new_task)
        db.session.commit()
        return make_response(jsonify({"data": new_task.serialize()}), 200)


@app.route("/course/<int:id>", methods=['PUT'])
def update_course(id):
    """Bonus points for validating the PUT body fields, including checking
       against the id in the URL
    """
    if request.method =='PUT':
        content =  request.get_json()
        if id != content['id']:
            return jsonify({"message": "The id does match the payload"})
        course = Course.query.get(id)
        course.description = content['description']
        course.image_path = content['image_path']
        course.on_discount = content['on_discount']
        course.price = content['price']
        course.title = content['title']
        course.date_updated = datetime.now().replace(microsecond=0)
        db.session.commit()
        return make_response(jsonify({"data": course.serialize()}), 200)




@app.route("/course/<int:id>", methods=['DELETE'])
def delete_course(id):
    
    if request.method =='DELETE':
        course = Course.query.get(id)
        exist = db.session.query(exists().where(Course.id == id)).scalar()
        if not exist:
            return jsonify({"messge": "Course "+str(id)+" does not exist"})
        db.session.delete(course)
        db.session.commit()
        return jsonify({"message": "The specified course was deleted"})

