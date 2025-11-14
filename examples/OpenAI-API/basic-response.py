# Basic Response Handling with OpenAI API and the Responses API

from openai import OpenAI

client = OpenAI()

# Set the model to use
model="gpt-5-nano"

# Default developer instructions
default_instructions = {
    "role": "developer",
    "content": "You are a friendly customer service representative for ShopFast, an e-commerce platform. Provide helpful, informative responses. Keep answers concise and professional."
}

# Customer asks a general question
response = client.responses.create(
    model=model,
    input=[
        default_instructions,
        {
            "role": "user",
            "content": "What's your return policy?"
        }
    ]
)

print(response.output_text)
