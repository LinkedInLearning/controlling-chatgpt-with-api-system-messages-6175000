# Custom Response Handling with OpenAI API and the Responses API

from openai import OpenAI

client = OpenAI()

# Set the model to use
model="gpt-5-nano"

# Default developer instructions
default_instructions = {
    "role": "developer",
    "content": "You are a friendly customer service representative for ShopFast, an e-commerce platform. Provide helpful, informative responses. Keep answers concise and professional."
}

def check_for_complaint(user_message):

    sentiment_check = client.responses.create(
        model=model,
        input=[
            {"role": "user", "content": f"Is this message a complaint or expressing frustration? Answer only 'yes' or 'no': {user_message}"}
        ]
    )
    
    return sentiment_check.output_text.strip().lower() == "yes"

# Get response with custom handling for complaints using the `instructions` parameter to override developer instructions
def get_response(user_message, conversation_history=[]):
    # Check for complaint
    is_complaint = check_for_complaint(user_message)

    # Build the input with conversation history
    messages = [default_instructions] + conversation_history + [
        {"role": "user", "content": user_message}
    ]
    
    # If complaint detected, override with empathetic instructions
    if is_complaint:
        response = client.responses.create(
            model=model,
            input=messages,
            instructions="""You are handling a customer complaint. Show genuine empathy and concern. Acknowledge their frustration explicitly. Focus on immediate resolution steps. Use phrases like 'I understand how frustrating this must be' and 'Let me help you resolve this right away.' Be apologetic and action-oriented."""
        )
    else:
        # Use default developer instructions (no override)
        response = client.responses.create(
            model=model,
            input=messages
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
    print(f"Response {idx}:\n{response.output_text}\n")