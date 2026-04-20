# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi! 😊"
    elif user_input == "how are you":
        return "I'm fine, thanks! How about you?"
    elif user_input == "bye":
        return "Goodbye! 👋"
    elif user_input == "thanks":
        return "You're welcome!"
    else:
        return "Sorry, I don't understand that."

def main():
    print("🤖 Chatbot started! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower() == "bye":
            break

# Run chatbot
main()