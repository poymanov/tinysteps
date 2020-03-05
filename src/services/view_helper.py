import services.days as days_service
import services.goals as goals_service
import services.teachers as teachers_service
from forms import BookingForm
from forms import RequestForm


def get_index_params():
    return {
        'teachers': teachers_service.get_random_teachers(6)
    }


def get_goal_params(goal_id):
    return {
        'teachers': teachers_service.get_teacher_by_goal(goal_id),
        'goal': goals_service.get_goal(goal_id)
    }


def get_profile_params(id):
    teacher = teachers_service.get_teacher_by_id(id)

    if teacher is None:
        return None

    goals = teachers_service.get_teacher_goals(teacher)
    free_hours = teachers_service.get_teacher_free_hours(teacher)

    return {
        'teacher': teacher,
        'goals': goals,
        'free_hours': free_hours
    }


def get_booking_params(teacher_id, hour, day_title):
    form = BookingForm()
    teacher = teachers_service.get_teacher_by_id(teacher_id)

    return {
        'form': form,
        'teacher': teacher,
        'hour': "{}".format(hour),
        'day': days_service.get_day_by_title(day_title)
    }


def get_booking_done_params(form):
    return {
        'hour': '{}:00'.format(form.clientTime.data),
        'day': days_service.get_day_by_id(form.clientWeekday.data),
        'client_name': form.clientName.data,
        'client_phone': form.clientPhone.data
    }


def get_request_params():
    form = RequestForm()
    return {
        'form': form,
    }


def get_request_done_params(request):
    return {
        'client_name': request.form.get('clientName'),
        'client_phone': request.form.get('clientPhone'),
        'time': request.form.get('time'),
        'goal_title': goals_service.get_goal(request.form.get('goal')).get('title')
    }
