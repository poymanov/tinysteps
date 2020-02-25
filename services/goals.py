import services.json_manager as json_manager


def get_goals():
    return json_manager.load_json(json_manager.read_json('data/goals.json'))


def get_goal(goal_id):
    goals = get_goals()

    for id, goal in goals.items():
        if id == goal_id:
            return goal

    return None
