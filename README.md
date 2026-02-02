# AI-judge
Structure of prompt (Reason)

    Split into 3 clear stages: intent, game logic, response, mirroring the assignment’s architecture requirement.

    All core rules (valid moves, bomb-only-once, bomb vs bomb, invalid/unclear = wasted turn) are written in natural language so the model, not code, makes the decisions.

    A strict JSON schema is defined (round, moves, status, winner, bomb state) so the judge output is structured and easy to consume from main.py.

Failure cases I considered

    User types nonsense or ambiguous text → marked INVALID/UNCLEAR, interpreted_intent = "none", user loses/wastes turn with explanation.

    User plays invalid moves ("book", "sofa") → explicitly invalid, not guessed into a valid move.

    User reuses bomb → treated as invalid, bomb not consumed again, bot wins with an explanation.

    Model overusing draws → rules explicitly say when draw is allowed (same move or bomb vs bomb), not when moves differ.

What I would improve next

    Add few-shot examples (sample rounds) inside the prompt to further stabilize JSON shape and edge-case behavior.

    Add lightweight JSON validation in code to catch missing or malformed fields and surface clearer errors.

    Make the bot strategy configurable (e.g., “bomb only when behind”) and pass that as context so the judge can explain bot behavior too.
