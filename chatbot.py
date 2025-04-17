# chatbot.py

def chatbot_response(user_input):
    """
    Simulated medical assistant response based on user input.
    You can later replace this with real AI or API integration.
    """
    # Simple logic for demo purposes
    user_input = user_input.lower()

    if "headache" in user_input:
        return "It sounds like you're experiencing a headache. Are you getting enough sleep and staying hydrated?"
    elif "fever" in user_input:
        return "You might be developing a fever. Monitor your temperature and stay hydrated. Consider consulting a doctor if it persists."
    elif "cough" in user_input:
        return "A persistent cough can have many causes. Are you experiencing any chest pain or shortness of breath?"
    else:
        return "Thank you for sharing. A medical professional can provide the best advice. Would you like help finding one?"
