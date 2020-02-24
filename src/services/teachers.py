import random

import services.json_reader as json_reader


def get_random_teachers(count):
    teachers = json_reader.load_json(json_reader.read_json('data/teachers.json'))
    random_teachers = {}
    teachers_length = len(teachers)

    while True:
        if len(random_teachers) == count:
            break

        random_teacher_id = random.randrange(1, teachers_length)
        existed_item = random_teachers.get(random_teacher_id)

        if existed_item is not None:
            continue

        random_teachers[random_teacher_id] = teachers[random_teacher_id]

    return random_teachers.values()
