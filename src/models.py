from common import db


class Request(db.Model):
    __tablename__ = "requests"

    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.String(255), nullable=False)
    time = db.Column(db.String(255), nullable=False)
    clientName = db.Column(db.String(255), nullable=False)
    clientPhone = db.Column(db.String(255), nullable=False)
