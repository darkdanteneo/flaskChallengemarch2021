"""Routines associated with the application data.
"""
import json
from run import db, Course
from datetime import datetime

courses = {}

def upload(content):
    id = content['id']
    description = content['description']
    image_path = content['image_path']
    on_discount = content['on_discount']
    price = content['price']
    title = content['title']

    date = content['date_created']
    date_created = datetime(int(date[0:4]), int(date[5:7]), int(date[8:10]), int(date[11:13]), int(date[14:16]), int(date[17:19]))
    date = content['date_updated']
    date_updated = datetime(int(date[0:4]), int(date[5:7]), int(date[8:10]), int(date[11:13]), int(date[14:16]), int(date[17:19]))
    
    
    new_task  = Course(id = id, description=description, image_path=image_path, on_discount=on_discount, price=price, title=title, date_created=date_created, date_updated=date_updated)
    db.session.add(new_task)
    db.session.commit()
    return content

def load_data():
    """Load the data from the json file.
    """
    with open('json/course.json', 'r') as filehandle:
        courses = json.load(filehandle)
        for x in courses:
            upload(x)
    pass


