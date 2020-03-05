def get_goal(goal_id):
    goals = get_goals()

    for id, goal in goals.items():
        if id == goal_id:
            return goal

    return None


def get_goals():
    return {
        'travel': {'icon': '⛱', 'title': 'Для путешествий'},
        'study': {'icon': '🏫', 'title': 'Для учебы'},
        'work': {'icon': '🏢', 'title': 'Для работы'},
        'relocate': {'icon': '🚜', 'title': 'Для переезда'}
    }
