from app import db


class Person(db.Model):
    __tablename__ = 'person'
    name = db.Column(db.String(20), primary_key=True, index=True)
    out_phone = db.Column(db.String(500), index=True)
