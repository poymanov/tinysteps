from common import db, Booking, Request


def save_teacher_booking(form):
    booking = Booking()
    form.populate_obj(booking)
    save_model(booking)


def save_teacher_request(form):
    request = Request()
    form.populate_obj(request)
    save_model(request)


def save_model(model):
    db.session.add(model)
    db.session.commit()
