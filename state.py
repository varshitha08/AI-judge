def initial_state():
    return {
        "round": 1,
        "user_bomb_used": False,
        "user_score": 0,
        "bot_score": 0,
    }


def compute_final_result(state):
    if state["user_score"] > state["bot_score"]:
        return "User wins"
    if state["user_score"] < state["bot_score"]:
        return "Bot wins"
    return "Draw"
