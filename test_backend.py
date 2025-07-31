import requests

query = {"query": "How to file an FIR?"}

response = requests.post("http://127.0.0.1:5000/get_legal_answer", json=query)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
