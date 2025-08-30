# app.py
# Backend for the Personal Finance Chatbot
# Technologies: Python, Streamlit, IBM Watson (placeholder), HuggingFace (placeholder)

# --- 1. SETUP and IMPORTS ---
import streamlit as st
import time

# --- MOCK IBM/HUGGINGFACE API FUNCTIONS ---
# In a real-world scenario, these functions would make API calls to IBM Watsonx.ai.
# You would use libraries like 'ibm_watsonx_ai' for this.
# For demonstration, we are simulating the API responses.

def get_ibm_model_response(user_input, demographic, chat_history):
    """
    (Placeholder) Simulates a call to an IBM generative AI model like Granite.

    This function constructs a system prompt based on the user's demographic
    and sends the query to the model to get a tailored response.

    Args:
        user_input (str): The user's latest message.
        demographic (str): The user's selected demographic ('Student' or 'Professional').
        chat_history (list): The history of the conversation.

    Returns:
        str: A simulated, tailored response from the AI model.
    """
    # 4.a. Demographic-Aware Communication: Tailor the AI's persona
    if demographic == 'Student':
        system_prompt = """
        You are a friendly and encouraging financial assistant for students.
        Your goal is to explain complex financial topics in a simple, relatable, and clear way.
        Avoid jargon. Use analogies related to student life. Keep the tone positive and supportive.
        Provide actionable, small steps.
        """
        # Example of a student-focused response
        if "investing" in user_input.lower():
            return "That's a great question! Think of investing like planting a tree. You start with a small seed (your initial investment), and over time, it can grow into something big! A good first step for students is to look into 'micro-investing' apps. They let you start with just a few dollars, like your spare change from buying coffee. It's a fantastic way to learn without needing a lot of money upfront!"
        elif "budget" in user_input.lower():
            return "Budgeting is super important, even with a student income! Let's make it simple. Try the 50/30/20 rule: 50% of your income for needs (like rent and groceries), 30% for wants (like going out with friends), and 20% for savings. We can create a sample budget based on your part-time job or allowance if you'd like!"
        else:
            return "I'm here to help you with your financial questions! As a student, understanding money is a real superpower. What's on your mind?"

    elif demographic == 'Professional':
        system_prompt = """
        You are a professional, concise, and data-driven financial analyst for working professionals.
        Provide clear, well-structured financial advice. You can refer to market trends,
        financial instruments, and tax implications. Your tone should be formal and respectful.
        Focus on efficiency, long-term growth, and portfolio optimization.
        """
        # Example of a professional-focused response
        if "investing" in user_input.lower():
            return "Certainly. For a professional, a diversified investment strategy is key. Based on your risk tolerance, we could explore a portfolio mix of ETFs (like those tracking the S&P 500), blue-chip stocks, and potentially some allocation to bonds for stability. Have you considered maximizing your tax-advantaged retirement accounts, such as a 401(k) or IRA, as a primary vehicle for long-term growth?"
        elif "tax" in user_input.lower():
            return "Navigating tax obligations is a critical component of financial planning. To provide accurate guidance, I would need to know more about your income sources, filing status, and any deductions or credits you might be eligible for. Key areas to consider for tax optimization include maximizing retirement contributions, leveraging tax-loss harvesting, and ensuring all eligible business expenses are deducted if you're self-employed."
        else:
            return "Welcome. I am ready to assist with your financial inquiries. How can I help you optimize your financial strategy today? We can discuss portfolio management, tax efficiency, or long-term savings goals."

    # Default fallback response
    return "I am a personal finance chatbot. Please select a profile to get started."


def generate_budget_summary(user_data, demographic):
    """
    (Placeholder) Simulates AI-powered budget summary generation.

    In a real application, you would pass structured data (e.g., from a CSV or form)
    to a generative model to create a narrative summary.

    Args:
        user_data (str): A string containing the user's financial data.
        demographic (str): The user's demographic for tailored tone.

    Returns:
        str: A simulated, narrative budget summary.
    """
    # The prompt would be something like:
    # "Analyze the following financial data and generate a budget summary.
    # Data: {user_data}"
    if demographic == 'Student':
        return "Got your numbers! Here’s a quick look: It seems like a good chunk of your spending is on 'Food & Dining,' which is totally normal for a student. One cool tip could be to try meal prepping – it can save you a surprising amount of cash! Your savings are off to a decent start. Keep it up!"
    else:
        return "Based on the data provided, here is a summary of your budget: The majority of your expenditure is allocated to 'Housing,' followed by 'Transportation.' Your discretionary spending appears to be within reasonable limits. There is a potential opportunity to increase your investment contributions by 10-15% by moderately reducing expenses in the 'Entertainment' category. This could accelerate progress towards your long-term financial goals."


# --- 2. STREAMLIT FRONTEND and LOGIC ---

# Page Configuration
st.set_page_config(
    page_title="Personal Finance Chatbot",
    page_icon="💰",
    layout="wide"
)

# --- UI Components ---
st.title(" Finance GenAI 🤖")
st.markdown("Your intelligent guide to savings, taxes, and investments, powered by IBM Watsonx.")

# Sidebar for User Profile Selection
with st.sidebar:
    st.header("👤 Your Profile")
    st.markdown("Select your profile to get personalized financial advice.")
    # 4.b. User selects their demographic
    user_demographic = st.radio(
        "Which of these best describes you?",
        ('Student', 'Professional'),
        key='demographic'
    )
    st.markdown("---")
    st.info("This chatbot is a demo. Financial advice is simulated and should not be taken as professional guidance.")


# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prior chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Main chat input and interaction logic
if prompt := st.chat_input("Ask about savings, budgets, or investments..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display AI response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Check for specific keywords to trigger different AI functions
        # 2. AI-Generated Budget Summaries & 3. Spending Insights
        if "summarize" in prompt.lower() or "budget" in prompt.lower() or "spending" in prompt.lower():
            # In a real app, you might ask the user to upload a file here
            # For demo, we use placeholder data
            sample_data = "Income: $1000/month, Rent: $400, Food: $300, Transport: $100, Entertainment: $150, Savings: $50"
            ai_response = generate_budget_summary(sample_data, st.session_state.demographic)
        else:
            # 1. Personalized Financial Guidance (General Q&A)
            # 5. Conversational NLP Experience
            ai_response = get_ibm_model_response(
                prompt,
                st.session_state.demographic,
                st.session_state.messages
            )

        # Simulate a streaming response for better UX
        for chunk in ai_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)

    # Add AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
