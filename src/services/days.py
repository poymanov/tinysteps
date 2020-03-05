def get_day_by_id(day_id):
    days = get_days()

    for day in days:
        if day['id'] == day_id:
            return day

    return None


def get_day_by_title(title):
    days = get_days()

    for day in days:
        if day['link_title'] == title:
            return day

    return None


def get_days():
    return [
        {
            'id': 'mon', 'title': 'Понедельник', 'link_title': 'monday'
        },
        {
            'id': 'tue', 'title': 'Вторник', 'link_title': 'tuesday'
        },
        {
            'id': 'wed', 'title': 'Среда', 'link_title': 'wednesday'
        },
        {
            'id': 'thu', 'title': 'Четверг', 'link_title': 'thursday'
        },
        {
            'id': 'fri', 'title': 'Пятница', 'link_title': 'friday'
        },
        {
            'id': 'sat', 'title': 'Суббота', 'link_title': 'saturday'
        },
        {
            'id': 'sun', 'title': 'Воскресение', 'link_title': 'sun'
        }
    ]
