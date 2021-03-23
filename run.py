"""Routes for the course resource.
"""

"""
-------------------------------------------------------------------------
Challenge general notes:
-------------------------------------------------------------------------

1. Bonus points for returning sensible HTTP codes from the API routes
2. Bonus points for efficient code (e.g. title search)
"""

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
# Import the API routes
from routes.course import *

db = SQLAlchemy(app)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    date_created = db.Column(db.String, default=datetime.now().replace(microsecond=0), nullable=False)
    date_updated = db.Column(db.String, default=datetime.now().replace(microsecond=0), nullable=False)
    description = db.Column(db.String(255))
    image_path = db.Column(db.String(100))
    on_discount = db.Column(db.Boolean, nullable=False)
    price = db.Column(db.Float, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    def serialize(self):
        return {"id": self.id,
                "date_created": self.date_created,
                "date_updated": self.date_updated,
                "description": self.description,
                "image_path": self.image_path,
                "on_discount": self.on_discount,
                "price": self.price,
                "title": self.title,}
    def __repr__(self):
        return "(%r, %r, %r, %r, %r, %r, %r, %r)" %(self.field1,self.dateCreated,self.dateUpdated,self.description,self.imagePath,self.onDiscount,self.price,self.title)


import data
# Required because app is imported in other modules
if __name__== '__main__':
    db.create_all()
    print("Loading data", end=" ")
    data.load_data()
    print("... done")
    app.run(debug=True)
