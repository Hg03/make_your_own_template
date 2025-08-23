import os
import streamlit as st
from huggingface_hub import InferenceClient

def execute(prompt: str):
    client = InferenceClient(
        provider="fireworks-ai",
        api_key=st.secrets["HF_TOKEN"],
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