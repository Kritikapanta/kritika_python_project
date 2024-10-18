# chatbot.py

def get_response(user_input):
    responses = {
        "hi": "Hello! How can I help you today?",
        "how are you?": "I'm just a program, but thanks for asking!",
        "what products do you have?": "We offer skincare, makeup, and haircare products.",
        "bye": "Goodbye! Have a great day!"
    }
    
    return responses.get(user_input.lower(), "I'm sorry, I don't understand that.")

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)
