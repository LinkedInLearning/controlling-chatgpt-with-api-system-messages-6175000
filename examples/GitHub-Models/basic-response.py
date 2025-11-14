# Basic Response with GitHub Models and the Chat Completions API

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

# Customer asks a general question
response = client.chat.completions.create(
    model=model,
    messages=[
        default_instructions,
        {
            "role": "user",
            "content": "What's your return policy?"
        }
    ]
)

print(response.choices[0].message.content)