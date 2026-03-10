
from groq import Groq

client = Groq(api_key="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")

messages = []

print("🤖 Chatbot ready! Type 'quit' to exit")
print("-" * 40)

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        print("Bye!")
        break
    
    messages.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    
    print(f"🤖 AI: {reply}")
    print("-" * 40)