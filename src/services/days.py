import services.json_reader as json_reader


def get_day_by_id(day_id):
    days = get_days()

    for day in days:
        if day['id'] == day_id:
            return day

    return None


def get_days():
    return json_reader.load_json(json_reader.read_json('data/days.json'))
