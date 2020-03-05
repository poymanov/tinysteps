import json

from sqlalchemy import func

import services.days as days_service
import services.goals as goals_service
from common import db, Teacher


def get_random_teachers(count):
    return db.session.query(Teacher).order_by(func.random()).limit(count).all()


def get_teacher_by_goal(goal):
    return db.session.query(Teacher).filter(Teacher.goals.like('%{}%'.format(goal))).order_by(Teacher.rating.desc()).all()


def get_teacher_by_id(teacher_id):
    return db.session.query(Teacher).get(teacher_id)


def get_teacher_goals(teacher):
    goals = []

    all_goals = goals_service.get_goals()
    teacher_goals = json.loads(teacher.goals)

    for teacher_goal in teacher_goals:
        goals.append(all_goals.get(teacher_goal).get('title'))

    return goals


def get_teacher_free_hours(teacher):
    free_hours = []

    teacher_free_hours = json.loads(teacher.free)

    for id, teacher_day in teacher_free_hours.items():
        day_info = days_service.get_day_by_id(id)

        if day_info is None:
            continue

        hours = []

        for hour, availability in teacher_day.items():
            if availability:
                hours.append({'title': hour, 'link': hour.split(':')[0]})

        day_free_hours = {'title': day_info.get('title'), 'link': day_info.get('link_title'), 'hours': hours}

        free_hours.append(day_free_hours)

    return free_hours
