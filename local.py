import requests

url = "https://ula-fumed-steadfastly.ngrok-free.dev/trivia"
response = requests.get(url).json()

print(response["question"]) 
for c in response.get("choices", []) or []:
    print(f"- {c}")
print(f"Answer: {response['answer']}")
