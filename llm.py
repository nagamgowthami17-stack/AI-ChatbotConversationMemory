
import ollama

def generate_response(message, conversation_history=None):
    messages = []

    if conversation_history:
        messages.extend(conversation_history)

    messages.append({
        "role": "user",
        "content": message
    })

    response = ollama.chat(
        model="qwen2.5-coder:7b",
        messages=messages
    )

    return response["message"]["content"]
