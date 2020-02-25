from flask import Flask, render_template, request

import services.feedback as feedback_service
import services.goals as goals_service
import services.view_helper as view_helper

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', params=view_helper.get_index_params())


@app.route('/goals/<goal>/')
def goal(goal):
    return render_template('goal.html', params=view_helper.get_goal_params(goal))


@app.route('/profiles/<id>/')
def profile(id):
    return render_template('profile.html', params=view_helper.get_profile_params(id))


@app.route('/booking/<teacher_id>/<day_title>/<hour>/', methods=['POST', 'GET'])
def booking(teacher_id, day_title, hour):
    if request.method == 'POST':
        feedback_service.save_teacher_booking(request.form)
        return render_template('booking_done.html',
                               params=view_helper.get_booking_done_params(day_title, hour, request))
    else:
        return render_template('booking.html', params=view_helper.get_booking_params(teacher_id, hour, day_title))


@app.route('/request/', methods=['POST', 'GET'])
def teacher_request():
    if request.method == 'POST':
        feedback_service.save_teacher_request(request.form)
        return render_template('request_done.html', params=view_helper.get_request_done_params(request))
    else:
        return render_template('request.html')


@app.context_processor
def global_data():
    return dict(goals=goals_service.get_goals())
