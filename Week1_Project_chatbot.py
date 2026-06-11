RESPONSES = {
    "hello": "Hello! I'm DecoBot. How can I help you today?",
    "hi": "Hi! How can I help?",
    "hey": "Hey! What can I do for you?",

    "bye": "Goodbye! Have a great day!",
    "goodbye": "See you later!",
    "see you": "Take care!",

    "how are you": "I'm doing well. How about you?",
    "what is your name": "I'm DecoBot, a rule-based chatbot.",
    "who are you": "I'm DecoBot, a chatbot built as part of the DecodeLabs AI internship.",

    "what is decodelabs": "DecodeLabs is a tech training organization that offers AI internship programs for students.",
    "contact": "Phone: +91 89330 06408 | Email: decodelabs.tech@gmail.com | Website: www.decodelabs.tech",

    "what is ai": "Artificial Intelligence is the simulation of human intelligence by machines.",
    "what is a chatbot": "A chatbot is a program that interacts with users through conversation.",
    "what is rule based ai": "Rule-based AI uses predefined rules to generate responses.",
    "what is machine learning": "Machine Learning is a branch of AI where systems learn patterns from data.",

    "help": "You can ask me about AI, DecodeLabs, or basic technology concepts. Type 'exit' to quit.",
    "what can you do": "I can answer a limited set of questions related to AI and DecodeLabs.",

    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs.",
    "thank you": "You're welcome!",
    "thanks": "No problem."
}

# Commands used to exit the chatbot
EXIT_COMMANDS = {"exit", "quit", "stop", "close", "q"}


def sanitize(user_input):
    return user_input.lower().strip()


def get_response(user_input):
    return RESPONSES.get(
        user_input,
        "Sorry, I don't understand that. Type 'help' to see what I can do."
    )


def run_chatbot():
    print("=" * 50)
    print("DecoBot - Rule-Based AI Chatbot")
    print("=" * 50)
    print("Type 'help' for assistance.")
    print("Type 'exit' to quit.")
    print("-" * 50)

    while True:
        user_input = input("\nYou: ")
        clean_input = sanitize(user_input)

        if clean_input in EXIT_COMMANDS:
            print("\nDecoBot: Goodbye!")
            break

        if clean_input == "":
            print("DecoBot: Please enter a message.")
            continue

        response = get_response(clean_input)
        print("DecoBot:", response)


if __name__ == "__main__":
    run_chatbot()
