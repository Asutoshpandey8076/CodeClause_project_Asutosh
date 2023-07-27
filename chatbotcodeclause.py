from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('CodeClauseBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English language corpus data
trainer.train('chatterbot.corpus.english')

# Function to get a response from the chatbot
def get_bot_response(user_input):
    return chatbot.get_response(user_input)

# Main loop for chatting with the bot
print("Code Clause Bot: Hello! How can I assist you today? (Type 'exit' to end the conversation.)")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Code Clause Bot: Goodbye! Have a great day!")
        break
    response = get_bot_response(user_input)
    print("Code Clause Bot:", response)
