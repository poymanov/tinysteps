from flask import Flask
from flask import render_template
import services.teachers as teachers_service

app = Flask(__name__)


@app.route('/')
def index():
    teachers = teachers_service.get_random_teachers(6)
    return render_template('index.html', teachers=teachers)
