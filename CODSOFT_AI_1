import re
import random
import datetime

def chatbot():
    print("🤖 Chatbot: Hello! I am your friendly chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input == "bye":
            print("🤖 Chatbot: Goodbye! Take care 😊")
            break

        # 1. Greetings
        elif re.search(r"\b(hi|hello|hey)\b", user_input):
            responses = [
                "Hello there! 👋",
                "Hey! How can I help you?",
                "Hi! Nice to see you here."
            ]
            print("🤖 Chatbot:", random.choice(responses))

        # 2. Asking about the chatbot
        elif "your name" in user_input:
            print("🤖 Chatbot: I am a simple chatbot created with Python.")

        elif "who created you" in user_input:
            print("🤖 Chatbot: I was created by a human who loves coding! 💻")

        # 3. How are you
        elif "how are you" in user_input:
            responses = [
                "I'm just code, but I'm doing great! 😃",
                "All good here! How about you?",
                "I’m fantastic! Thanks for asking."
            ]
            print("🤖 Chatbot:", random.choice(responses))

        # 4. Time and Date
        elif "time" in user_input:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"🤖 Chatbot: The current time is {now}")

        elif "date" in user_input:
            today = datetime.date.today().strftime("%B %d, %Y")
            print(f"🤖 Chatbot: Today's date is {today}")

        # 5. Weather (fake response for demo)
        elif "weather" in user_input:
            responses = [
                "It’s always sunny in my virtual world! ☀️",
                "I don’t have weather sensors, but I hope it’s nice outside!",
                "Cloudy with a chance of bugs 🐞"
            ]
            print("🤖 Chatbot:", random.choice(responses))

        # 6. Jokes
        elif "joke" in user_input:
            jokes = [
                "Why don’t programmers like nature? It has too many bugs! 😂",
                "What do you call 8 hobbits? A hobbyte. 😆",
                "Why was the math book sad? Because it had too many problems."
            ]
            print("🤖 Chatbot:", random.choice(jokes))

        # 7. Help
        elif "help" in user_input:
            print("🤖 Chatbot: You can ask me about time, date, weather, jokes, or just say hello!")

        # 8. Fallback
        else:
            print("🤖 Chatbot: Hmm... I don't understand that yet. Try asking something else.")

# Run the chatbot
chatbot()

