# app.py
# Backend for the Personal Finance Chatbot using FLASK

from flask import Flask, render_template, request, jsonify
import time

# --- 1. SETUP ---
# Initialize the Flask app
app = Flask(__name__)

# --- 2. YOUR ORIGINAL AI LOGIC (COPIED FROM YOUR STREAMLIT SCRIPT) ---
# No changes are needed in these functions.
def get_ibm_model_response(user_input, demographic, chat_history):
    """
    (Placeholder) Simulates a call to an IBM generative AI model.
    """
    if demographic == 'Student':
        if "investing" in user_input.lower():
            return "That's a great question! Think of investing like planting a tree. You start with a small seed (your initial investment), and over time, it can grow into something big! A good first step for students is to look into 'micro-investing' apps. They let you start with just a few dollars, like your spare change from buying coffee. It's a fantastic way to learn without needing a lot of money upfront!"
        elif "budget" in user_input.lower():
            return "Budgeting is super important, even with a student income! Let's make it simple. Try the 50/30/20 rule: 50% of your income for needs (like rent and groceries), 30% for wants (like going out with friends), and 20% for savings. We can create a sample budget based on your part-time job or allowance if you'd like!"
        else:
            return "I'm here to help you with your financial questions! As a student, understanding money is a real superpower. What's on your mind?"

    elif demographic == 'Professional':
        # Prepare the user's input once to make the checks cleaner
        clean_input = user_input.lower()

        # Check for multiple related keywords
        if "investing" in clean_input or "investment" in clean_input:
            return "Certainly. For a professional, a diversified investment strategy is key..."
        
        # You can improve the other checks too
        elif "tax" in clean_input or "taxes" in clean_input:
            return "Navigating tax obligations is a critical component of financial planning..."
        
        else:
            return "Welcome. I am ready to assist with your financial inquiries..."
    
# --- 3. FLASK ROUTES (THE "API") ---

# This route serves your main landing page (index.html)
@app.route('/')
def home():
    return render_template('index.html')

# This route will serve the new chat page when you click "Get Started"
@app.route('/chat')
def chat_page():
    return render_template('chat.html')

# This is the API endpoint for the chatbot logic.
# The chat.html page will send messages here.
@app.route('/get_response', methods=['POST'])
# ... (rest of your app.py code) ...

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    # ADD THIS LINE TO SEE ALL DATA RECEIVED FROM THE BROWSER
    print(f"DEBUG: Received data from frontend: {data}")

    user_message = data.get('message')
    demographic = data.get('demographic', 'Professional')
    chat_history = data.get('history', [])
    
    # ADD THIS LINE TO SEE THE EXTRACTED MESSAGE
    print(f"DEBUG: Extracted user_message: '{user_message}'")

    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    # Get the AI response from your function
    ai_response = get_ibm_model_response(user_message, demographic, chat_history)

    # Return the response to the frontend
    return jsonify({'response': ai_response})

# ... (rest of your app.py code) ...

# --- 4. RUN THE APP ---
if __name__ == '__main__':
    
    app.run(debug=True)