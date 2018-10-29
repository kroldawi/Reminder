from app import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    when = db.Column(db.Date)
    recurring = db.Column(db.Boolean)
