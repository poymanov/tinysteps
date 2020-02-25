import services.json_manager as json_manager


def save_teacher_booking(lesson_params):
    booking_file_path = 'data/feedback/teachers-booking.json'
    booking = json_manager.load_json(json_manager.read_json(booking_file_path))
    booking.append(lesson_params)
    json_manager.save_json(booking_file_path, json_manager.dump_json(booking))
