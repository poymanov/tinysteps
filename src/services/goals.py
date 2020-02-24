import services.json_reader as json_reader


def get_goals():
    return json_reader.load_json(json_reader.read_json('data/goals.json'))


def get_goal_title(goal):
    goals = get_goals()

    for id, title in goals.items():
        if id == goal:
            return goals[id]

    return None
