from flask import Flask
from flask import render_template

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


@app.context_processor
def global_data():
    return dict(goals=goals_service.get_goals())
