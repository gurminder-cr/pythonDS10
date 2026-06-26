from ollama import chat
# pip install ollama
que= input("Enter Question ")

response = chat(
    model='gemma3:1b',
    messages=[{'role': 'user', 'content': que}],
)
print(response.message.content)