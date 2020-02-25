import services.json_manager as json_manager


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
    return json_manager.load_json(json_manager.read_json('data/days.json'))
