from groq import Groq
import os

client = Groq(api_key="your_key_here")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Say hello and introduce yourself in 2 lines!"}
    ]
)

print(response.choices[0].message.content)