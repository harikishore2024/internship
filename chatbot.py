def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")

    while True:
        user_input = input("You: ").lower()

        if 'hello' in user_input or 'hi' in user_input:
            print("Bot: Hello! How can I assist you?")
        elif 'how are you' in user_input:
            print("Bot: I'm just a bot, but I'm doing great! How about you?")
        elif 'your name' in user_input:
            print("Bot: I am a chatbot, and I don't have a name.")
        elif 'bye' in user_input or 'goodbye' in user_input:
            print("Bot: Goodbye! Have a great day!")
            break
        elif 'thank you' in user_input or 'thanks' in user_input:
            print("Bot: You're welcome! Let me know if you need anything else.")
        elif 'weather' in user_input:
            print("Bot: I can't check the weather right now, but you can check your local forecast!")
        elif 'help' in user_input:
            print("Bot: Sure, I can assist you with basic queries like 'how are you', 'weather', etc.")
        else:
            print("Bot: Sorry, I didn't quite understand that. Can you please ask something else?")

if __name__ == "__main__":
    chatbot()
