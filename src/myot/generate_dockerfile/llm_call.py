import os
from dotenv import load_dotenv
load_dotenv()
from huggingface_hub import InferenceClient

def execute(prompt: str):
    client = InferenceClient(
        provider="fireworks-ai",
        api_key=os.getenv("HF_TOKEN"),
    )

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    return completion.choices[0].message