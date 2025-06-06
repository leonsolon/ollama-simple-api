from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(
    model="llama3.1:8b",
    messages=[
        {
            "role": "user",
            "content": "Resuma em um parágrafo a evolução da inteligência artificial como descrito na obra Eu, Robô! de Isaac Asimov"
        },
    ],
)
print(response["message"]["content"])
# or access fields directly from the response object
print(response.message.content)
