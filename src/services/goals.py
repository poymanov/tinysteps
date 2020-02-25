import services.json_manager as json_manager


def get_goals():
    return json_manager.load_json(json_manager.read_json('data/goals.json'))


def get_goal_title(goal):
    goals = get_goals()

    for id, title in goals.items():
        if id == goal:
            return goals[id]

    return None
