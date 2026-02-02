import json
import random
import os
from google import genai
from prompts import SYSTEM_PROMPT

MODEL_NAME = "gemini-3-flash-preview"

# No hardcoding: read from environment
API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is not set in the environment")

client = genai.Client(api_key=API_KEY)



def pick_bot_move():
    # Simple bot: bomb is rare
    if random.random() < 0.2:
        return "bomb"
    return random.choice(["rock", "paper", "scissors"])


def judge_move(user_input: str, state: dict):
    bot_move = pick_bot_move()

    full_prompt = f"""
{SYSTEM_PROMPT}

====================
ROUND CONTEXT
====================

Round Number: {state['round']}
User bomb already used: {state['user_bomb_used']}
Bot move: {bot_move}

User input:
"{user_input}"
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[full_prompt],
    )

    text = response.text.strip()

    try:
        result = json.loads(text)
    except json.JSONDecodeError:
        raise ValueError(f"Model did not return valid JSON. Got:\n{text}")

    # Update state from model result
    if result.get("bomb_consumed", False):
        state["user_bomb_used"] = True

    if result.get("round_winner") == "user":
        state["user_score"] += 1
    elif result.get("round_winner") == "bot":
        state["bot_score"] += 1

    state["round"] += 1

    # Ensure state_update matches state
    result["state_update"] = {
        "user_bomb_available": not state["user_bomb_used"]
    }

    return result
