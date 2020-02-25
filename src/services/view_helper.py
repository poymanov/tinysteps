import services.days as days_service
import services.goals as goals_service
import services.teachers as teachers_service


def get_index_params():
    return {
        'teachers': teachers_service.get_random_teachers(6)
    }


def get_goal_params(goal):
    return {
        'teachers': teachers_service.get_teacher_by_goal(goal),
        'goal_title': goals_service.get_goal_title(goal)
    }


def get_profile_params(id):
    teacher = teachers_service.get_teacher_by_id(id)
    goals = teachers_service.get_teacher_goals(teacher)
    free_hours = teachers_service.get_teacher_free_hours(teacher)

    return {
        'teacher': teacher,
        'goals': goals,
        'free_hours': free_hours
    }


def get_booking_params(teacher_id, hour, day_title):
    teacher = teachers_service.get_teacher_by_id(teacher_id)

    return {
        'teacher': teacher,
        'hour': "{}:00".format(hour),
        'day': days_service.get_day_by_title(day_title)
    }


def get_booking_done_params(day_title, hour, request):
    return {
        'hour': '{}:00'.format(hour),
        'day': days_service.get_day_by_title(day_title),
        'client_name': request.form.get('clientName'),
        'client_phone': request.form.get('clientPhone')
    }


def get_request_done_params(request):
    return {
        'client_name': request.form.get('clientName'),
        'client_phone': request.form.get('clientPhone'),
        'time': request.form.get('time'),
        'goal_title': goals_service.get_goal_title(request.form.get('goal'))
    }
