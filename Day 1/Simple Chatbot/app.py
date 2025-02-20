# Import the regular expression module to handel pattern matching

import re

# Define a dictionary containing a few responses
responses = {
    "Tell me something about linear regression": "Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables by fitting a linear equation to the data. It aims to minimize the difference between predicted and actual values using techniques like Ordinary Least Squares (OLS).",    
    "hello": "Hello! I'm Raymond, how can i help you?",
    "hi": "Hello! I'm Raymond, how can i help you?",
    "how are you": "I'm doing great! How about you?",
    "what is your name": "I'm a Raymond.",
    "help": "Sure, I'm here to help. What do you need assistance with?",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! I'm happy to help.",
    "default": "I'm sorry, I don't understand. Can you please rephrase your query?"
    
}

# Function to find the appropriate response based on the user's input
def chatbot_response(user_input):
    # Convert user input to lowercase to make matching case-insensitive
    user_input = user_input.lower()
    
    for keyword in responses:
        # Use regular expression to search for the keyword in the user input
        if re.search(keyword.lower(), user_input):
            return responses[keyword]

    # If no keyword matches, return the default response
    return responses["default"]

# Main function to run the chatbot
def chatbot():
    print("Welcome to Raymond's Chatbot!")
    print("You can start chatting with me. Type 'exit' to end the conversation.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # If user types 'exit' or 'bye', end the conversation
        if user_input.lower() == "exit" or user_input.lower() == "bye":
            print("Raymond: Goodbye! Have a great day.")
            break

        # Get the chatbot response based on user input
        response = chatbot_response(user_input)
        
        # Print the response
        print(f"Raymond: {response}")
        
chatbot()