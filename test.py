from groq import Groq
import os

client = Groq(api_key="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")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Say hello and introduce yourself in 2 lines!"}
    ]
)

print(response.choices[0].message.content)