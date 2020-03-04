import services.json_manager as json_manager
from common import db
from models import Request


def save_teacher_booking(lesson_params):
    booking_file_path = 'data/feedback/teachers-booking.json'
    save_feedback_data(booking_file_path, lesson_params)


def save_teacher_request(form):
    request = Request()

    form.populate_obj(request)

    db.session.add(request)
    db.session.commit()


def save_feedback_data(file_path, data):
    existed_data = json_manager.load_json(json_manager.read_json(file_path))
    existed_data.append(data)
    json_manager.save_json(file_path, json_manager.dump_json(existed_data))
