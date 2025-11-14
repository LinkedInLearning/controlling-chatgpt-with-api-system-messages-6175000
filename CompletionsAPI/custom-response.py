# Custom Response Handling with GitHub Models and the Chat Completions API

import os
from openai import OpenAI


token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-5-nano"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Default developer instructions
default_instructions = {
    "role": "developer",
    "content": "You are a friendly customer service representative for ShopFast, an e-commerce platform. Provide helpful, informative responses. Keep answers concise and professional."
}

complaint_instructions = """You are handling a customer complaint. Show genuine empathy and concern. Acknowledge their frustration explicitly. Focus on immediate resolution steps. Use phrases like 'I understand how frustrating this must be' and 'Let me help you resolve this right away.' Be apologetic and action-oriented."""

def check_for_complaint(user_message):

    sentiment_check = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": f"Is this message a complaint or expressing frustration? Answer only 'yes' or 'no': {user_message}"}
        ]
    )
    
    return sentiment_check.choices[0].message.content.strip().lower() == "yes"

def get_response(user_message, conversation_history=[]):
    # Check for complaint
    is_complaint = check_for_complaint(user_message)

    # Build the input with conversation history
    developer_message = default_instructions if not is_complaint else {
        "role": "developer",
        "content": complaint_instructions
    }

    messages = [developer_message] + conversation_history + [
        {"role": "user", "content": user_message}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    
    return response

# Example usage

# Loop through sample test messages
test_messages = [
    "How long does shipping usually take?",
    "I'm very disappointed. My order arrived broken and customer service hasn't responded!"
]

for idx, message in enumerate(test_messages, start=1):
    print(f"Processing message {idx}: '{message}'...")
    response = get_response(message)
    print(f"Response {idx}:\n{response.choices[0].message.content}\n")