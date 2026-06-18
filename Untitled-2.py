def chatbot():
    print("🤖 ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello" or user == "hi":
            print("🤖 ChatBot: Hello! How are you?")
        elif "how are you" in user:
            print("🤖 ChatBot: I'm doing great! Thanks for asking.")
        elif "your name" in user:
            print("🤖 ChatBot: My name is Cookie.")
        elif "help" in user:
            print("🤖 ChatBot: I can chat with you. Try asking me something!")
        elif user == "bye":
            print("🤖 ChatBot: Goodbye! Have a great day.")
            break
        else:
            print("🤖 ChatBot: Sorry, I don't understand that.")

chatbot()