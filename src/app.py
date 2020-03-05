from flask import render_template, request

import services.feedback as feedback_service
import services.goals as goals_service
import services.view_helper as view_helper
from common import app, abort
from forms import BookingForm, RequestForm


@app.route('/')
def index():
    return render_template('index.html', params=view_helper.get_index_params())


@app.route('/goals/<goal>/')
def goal(goal):
    return render_template('goal.html', params=view_helper.get_goal_params(goal))


@app.route('/profiles/<id>/')
def profile(id):
    params = view_helper.get_profile_params(id)

    if params is None:
        abort(404)

    return render_template('profile.html', params=params)


@app.route('/booking/<teacher_id>/<day_title>/<hour>/', methods=['GET'])
def booking_form(teacher_id, day_title, hour):
    return render_template('booking.html', params=view_helper.get_booking_params(teacher_id, hour, day_title))


@app.route('/booking/<teacher_id>/<day_title>/<hour>/', methods=['POST'])
def booking(teacher_id, day_title, hour):
    form = BookingForm()

    if form.validate_on_submit():
        feedback_service.save_teacher_booking(form)
        params = view_helper.get_booking_done_params(form)
        return render_template('booking_done.html', params=params)
    else:
        params = view_helper.get_booking_params(teacher_id, hour, day_title)
        params['form'] = form
        return render_template('booking.html', params=params)


@app.route('/request/', methods=['GET'])
def teacher_request_form():
    return render_template('request.html', params=view_helper.get_request_params())


@app.route('/request/', methods=['POST'])
def teacher_request():
    form = RequestForm()

    if form.validate_on_submit():
        feedback_service.save_teacher_request(form)
        return render_template('request_done.html', params=view_helper.get_request_done_params(request))
    else:
        return render_template('request.html', params={'form': form})


@app.context_processor
def global_data():
    return dict(goals=goals_service.get_goals())


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')
