from common import db


class Request(db.Model):
    __tablename__ = "requests"

    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.String(255), nullable=False)
    time = db.Column(db.String(255), nullable=False)
    clientName = db.Column(db.String(255), nullable=False)
    clientPhone = db.Column(db.String(255), nullable=False)


class Teacher(db.Model):
    __tablename__ = "teachers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    about = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    picture = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    goals = db.Column(db.Text, nullable=False)
    free = db.Column(db.Text, nullable=False)


class Booking(db.Model):
    __tablename__ = "booking"

    id = db.Column(db.Integer, primary_key=True)
    clientName = db.Column(db.String(255), nullable=False)
    clientPhone = db.Column(db.String(255), nullable=False)
    clientWeekday = db.Column(db.String(3), nullable=False)
    clientTime = db.Column(db.Integer, nullable=False)
    clientTeacherId = db.Column(db.Integer, db.ForeignKey('teachers.id'))

    clientTeacher = db.relationship('Teacher')
