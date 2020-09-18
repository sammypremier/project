from flask_sqlalchemy import SQLAlchemy
from pelox import db

class Ordinaryuser(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(120), nullable = False)
    email = db.Column(db.String(120), nullable = False, unique = True)
    password = db.Column(db.String(100), nullable = False)
    image = db.Column(db.String(60), nullable = False, default = 'default.jpg')

    def __repr__ (self):
        return f"Ordinaryuser('{self.username}', '{self.email}', '{self.image}')"    

class Post(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(20), nullable = False)
    price = db.Column(db.String(10), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    landing_page_image = db.Column(db.String(60))
    first_slider_image = db.Column(db.String(60))
    first_post_image = db.Column(db.String(60))
    second_slider_image = db.Column(db.String(60))
    second_post_image = db.Column(db.String(60))
    third_slider_image = db.Column(db.String(60))
    third_post_image = db.Column(db.String(60))

    def __repr__ (self):
        return f"Post('{self.id}', '{self.landing_page_image}, {self.first_slider_image}','{self.first_post_image}', '{self.second_slider_image}','{self.second_slider_image}', '{self.third_slider_image}','{self.third_post_image}')"
