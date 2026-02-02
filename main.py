import json
from judge_client import judge_move
from state import initial_state, compute_final_result


def main():
    state = initial_state()
    print("Rock-Paper-Scissors Plus - AI Judge (type 'quit' to exit)\n")

    while True:
        user_input = input("Your move: ").strip()
        if user_input.lower() == "quit":
            break

        try:
            result = judge_move(user_input, state)
        except Exception as e:
            print("Error talking to the model:", e)
            break

        print("\n-----ROUND RESULT-----")
        print(json.dumps(result, indent=2))
        print("----------------------\n")

    print("Final Score: ")
    print(f"User: {state['user_score']} | Bot: {state['bot_score']}")
    print("Final Result:", compute_final_result(state))


if __name__ == "__main__":
    main()
