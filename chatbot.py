import nltk
import random

nltk.download('punkt')

intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening"],
        "responses": ["Hello!", "Hi there!", "Hey! How can I help you?"]
    },
    "goodbye": {
        "patterns": ["bye", "see you", "goodbye"],
        "responses": ["Goodbye!", "See you later!", "Have a nice day!"]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "thx"],
        "responses": ["You're welcome!", "No problem!", "Glad I could help!"]
    },
    "about": {
        "patterns": ["who are you?", "what are you?", "about yourself"],
        "responses": ["I am a simple chatbot created in Python!", "I am your Python chatbot assistant."]
    }
}

def match_intent(user_input):
    user_input = user_input.lower()
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if pattern.lower() in user_input:
                return random.choice(data["responses"])
    return "I am sorry, I didn't understand that."

print("Chatbot: Hello! Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot: Goodbye!")
        break
    response = match_intent(user_input)
    print(f"Chatbot: {response}")
