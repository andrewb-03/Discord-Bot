from random import choice, randint

def get_response(user_input: str) -> str:
    lowered = user_input.lower()

    # list of common greetings
    greetings = ["hello", "hi", "hey", "what's up", "whats up",]

    # response if input is empty or only whitespace
    if not lowered.strip():
        return "Well, you're quiet..."

    # checks if any greeting is in the user input
    elif any(greeting in lowered for greeting in greetings):
        return choice(["Hi!", "Hello!", "Hey there!"])

    elif "how are you" in lowered:
        return "I'm good, I think?"

    elif "bye" in lowered or "goodbye" in lowered:
        return "See you later!"

    elif "roll dice" in lowered:
        return f"Sure! You rolled: {randint(1, 6)}"

    elif "roll again" in lowered:
        return f"You rolled: {randint(1, 6)}"

    elif "flip a coin" in lowered:
        return choice(["Heads.", "Tails."])

    else:
        return choice([
            "I do not understand... sorry. Try again.",
            "What are you talking about?",
            "Do you mind rephrasing that?",
            "I'm not quite sure what you mean."
        ])