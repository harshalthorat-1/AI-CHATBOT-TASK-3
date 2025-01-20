import spacy
import random

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Predefined intents with examples and responses
intents = {
    "greeting": {
        "examples": ["hello", "hi", "hey", "good morning", "good evening"],
        "responses": ["Hello!", "Hi there!", "Greetings!", "Good to see you!"]
    },
    "goodbye": {
        "examples": ["bye", "goodbye", "see you later", "farewell", "catch you later"],
        "responses": ["Goodbye!", "See you later!", "Take care!", "Farewell!"]
    },
    "thanks": {
        "examples": ["thank you", "thanks", "much appreciated", "thanks a lot", "thanks a ton"],
        "responses": ["You're welcome!", "No problem!", "Happy to help!", "Anytime!"]
    },
    "weather": {
        "examples": ["what's the weather like?", "weather report", "current weather", "is it raining?"],
        "responses": ["I'm not sure, but you can check a weather app!", "It's always sunny in my world!", "I recommend checking your local weather forecast."]
    },
    "help": {
        "examples": ["help", "can you help me?", "i need assistance", "support", "help me please"],
        "responses": ["Sure, how can I assist you?", "I'm here to help!", "What do you need help with?", "Feel free to ask me anything."]
    },
    "joke": {
        "examples": ["tell me a joke", "make me laugh", "do you know any jokes?", "joke"],
        "responses": ["Why don't scientists trust atoms? Because they make up everything!", "What do you get when you cross a snowman and a vampire? Frostbite!", "Why did the scarecrow win an award? Because he was outstanding in his field!"]
    },
   "quote": {
        "examples": ["give me a quote", "quote of the day", "inspire me", "motivate me"],
        "responses": ["The best time to plant a tree was 20 years ago. The second best time is now.", "Your limitation—it’s only your imagination.", "Push yourself, because no one else is going to do it for you."]
    },
    "time": {
        "examples": ["what time is it?", "current time", "tell me the time", "time now"],
        "responses": ["I can't tell time, but you can check your device's clock!", "Time flies when you're having fun!", "Check your watch or phone for the time!"]
    },
    "date": {
        "examples": ["what's the date today?", "current date", "tell me the date", "date today"],
        "responses": ["I'm not sure of the exact date, but you can check your calendar!", "Every day is a new adventure!", "Check your device for the date!"]
    },
    "news": {
        "examples": ["tell me the news", "latest news", "what's happening in the world?", "news update"],
        "responses": ["I'm not up-to-date with the latest news, but you can check your favorite news site!", "The world is full of stories. Check a news app for updates!", "I recommend visiting a news website for the latest updates."]
    },
    "food_recommendation": {
        "examples": ["what should I eat?", "recommend a dish", "suggest some food", "food ideas"],
        "responses": ["How about trying some pizza?", "A fresh salad could be a great choice!", "You can never go wrong with pasta!", "Maybe a nice sandwich?"]
    },
    "movie_recommendation": {
        "examples": ["suggest a movie", "what movie should I watch?", "movie recommendations", "what's a good movie?"],
        "responses": ["How about watching 'Inception'?", "If you like comedy, try 'The Grand Budapest Hotel'!", "'Interstellar' is a great sci-fi movie!", "You might enjoy 'Parasite'."]
    },
    "sports_update": {
        "examples": ["what's the latest sports news?", "sports update", "who won the game?", "sports scores"],
        "responses": ["I'm not sure about the latest scores, but you can check a sports website!", "Sports are exciting! Check the latest updates online.", "I recommend checking a sports app for the latest scores."]
    },
    "music_recommendation": {
        "examples": ["suggest a song", "what music should I listen to?", "music recommendations", "song ideas"],
        "responses": ["You should check out 'Blinding Lights' by The Weeknd!", "'Shape of You' by Ed Sheeran is a great song!", "Try listening to 'Levitating' by Dua Lipa.", "'Bohemian Rhapsody' by Queen is a classic!"]
    },
    "compliment": {
        "examples": ["give me a compliment", "say something nice", "compliment me", "flatter me"],
        "responses": ["You're doing great!", "You're amazing!", "You're capable of achieving anything!", "You have a great sense of style!"]
    },
    "fact": {
        "examples": ["tell me a fact", "interesting fact", "did you know?", "random fact"],
        "responses": ["Did you know? Honey never spoils.", "Octopuses have three hearts.", "Bananas are berries, but strawberries aren't!", "The Eiffel Tower can be 15 cm taller during the summer."]
    },
    "travel_recommendation": {
        "examples": ["where should I travel?", "travel suggestions", "recommend a place to visit", "vacation ideas"],
        "responses": ["You should visit the Maldives for a tropical getaway!", "How about exploring the historic streets of Rome?", "Japan offers a unique mix of tradition and modernity!", "Consider a trip to New Zealand for breathtaking landscapes."]
    }
}

# Function to get the intent from user input
def get_intent(text):
    doc = nlp(text.lower())
    for intent, data in intents.items():
        for example in data["examples"]:
            if example in text.lower():
                return intent
    return None

# Function to get a response based on the intent
def get_response(intent):
    if intent in intents:
        return random.choice(intents[intent]["responses"])
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"

# Main chatbot function
def chatbot_response(user_input):
    intent = get_intent(user_input)
    return get_response(intent)

# Running the chatbot in a loop
def main():
    print("Chatbot: Hello! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
