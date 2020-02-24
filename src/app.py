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


@app.context_processor
def global_data():
    return dict(goals=goals_service.get_goals())
