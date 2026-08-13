from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file  

from anthropic import Anthropic

client = Anthropic(api_key="ANTHROPIC_API_KEY")  # Replace with your actual API key
model = "claude-sonnet-4-5"  # Specify the model you want to use

client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "Write a short poem about the beauty of nature."
        }
    ]
)
