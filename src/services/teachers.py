import random

import services.days as days_service
import services.goals as goals_service
import services.json_reader as json_reader


def get_random_teachers(count):
    teachers = get_teachers()
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


def get_teacher_by_id(teacher_id):
    teachers = get_teachers()

    for teacher in teachers:
        if int(teacher.get('id')) == int(teacher_id):
            return teacher

    return None


def get_teacher_goals(teacher):
    goals = []

    all_goals = goals_service.get_goals()

    for teacher_goal in teacher.get('goals'):
        goals.append(all_goals.get(teacher_goal))

    return goals


def get_teacher_free_hours(teacher):
    free_hours = []

    for id, teacher_day in teacher.get("free").items():
        day_info = days_service.get_day_by_id(id)

        if day_info is None:
            continue

        hours = []

        for hour, availability in teacher_day.items():
            if availability:
                hours.append({'title': hour, 'link': hour[0]})

        day_free_hours = {'title': day_info.get('title'), 'link': day_info.get('link_title'), 'hours': hours}

        free_hours.append(day_free_hours)

    return free_hours


def get_teachers():
    return json_reader.load_json(json_reader.read_json('data/teachers.json'))
