from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, RadioField
from wtforms.validators import InputRequired, Length

import services.goals as goals_service


class BookingForm(FlaskForm):
    clientName = StringField('Вас зовут', [InputRequired(), Length(min=3, message='Не менее 3 символов')])
    clientPhone = StringField('Ваш телефон', [InputRequired(), Length(min=5, message='Не менее 5 символов')])
    clientWeekday = HiddenField('clientWeekday', [InputRequired()])
    clientTime = HiddenField('clientTime', [InputRequired()])
    clientTeacher = HiddenField('clientTeacher', [InputRequired()])


class RequestForm(FlaskForm):
    goals = goals_service.get_goals()
    goals_choices = []

    for id, goal in goals.items():
        goals_choices.append((id, goal.get('title')))

    clientName = StringField('Вас зовут', [InputRequired(), Length(min=3, message='Не менее 3 символов')])
    clientPhone = StringField('Ваш телефон', [InputRequired(), Length(min=5, message='Не менее 5 символов')])
    goal = RadioField('Какая цель занятий?', [InputRequired(message='Обязательное поле')], choices=goals_choices, default='travel')
    time = RadioField('Сколько времени есть?', [InputRequired(message='Обязательное поле')],
                      choices=[('1-2', '1-2 часа в неделю'), ('3-5', '3-5 часов в неделю'),
                               ('5-7', '5-7 часов в неделю'), ('7-10', '7-10 часов в неделю')], default='5-7')
