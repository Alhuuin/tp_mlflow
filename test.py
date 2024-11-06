import requests

url = "http://127.0.0.1:8000/predict"
payload = {"data": [[5.1, 3.5, 1.4, 0.2], [6.7, 3.1, 4.7, 1.5]]}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.json())

