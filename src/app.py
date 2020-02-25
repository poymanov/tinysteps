from flask import Flask, render_template, request

import services.days as days_service
import services.feedback as feedback_service
import services.goals as goals_service
import services.teachers as teachers_service

app = Flask(__name__)


@app.route('/')
def index():
    teachers = teachers_service.get_random_teachers(6)
    return render_template('index.html', teachers=teachers)


@app.route('/goals/<goal>/')
def goal(goal):
    teachers = teachers_service.get_random_teachers(6)
    goal_title = goals_service.get_goal_title(goal)
    return render_template('goal.html', teachers=teachers, goal_title=goal_title)


@app.route('/profiles/<id>/')
def profile(id):
    teacher = teachers_service.get_teacher_by_id(id)
    goals = teachers_service.get_teacher_goals(teacher)
    free_hours = teachers_service.get_teacher_free_hours(teacher)
    return render_template('profile.html', teacher=teacher, goals=goals, free_hours=free_hours)


@app.route('/booking/<teacher_id>/<day_title>/<hour>/', methods=['POST', 'GET'])
def booking(teacher_id, day_title, hour):
    day = days_service.get_day_by_title(day_title)
    if request.method == 'POST':
        feedback_service.save_teacher_booking(request.form)
        return render_template('booking_done.html', hour=hour, day=day, client_name=request.form.get('clientName'),
                               client_phone=request.form.get('clientPhone'))
    else:
        teacher = teachers_service.get_teacher_by_id(teacher_id)
        return render_template('booking.html', teacher=teacher, hour=hour, day=day)


@app.context_processor
def global_data():
    return dict(goals=goals_service.get_goals())
