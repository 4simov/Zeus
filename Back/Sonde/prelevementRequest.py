import requests

baseUrl = "http://127.0.0.1:5000"

def test():
	print("test")

def send():
	r = requests.post(baseUrl + 're', json={
  		"temperature": "Jason Sweet",
  		"Quantity": 1,
  		"time": 18.00
	})
	print(f"Status Code: {r.status_code}, Response: {r.json()}")
