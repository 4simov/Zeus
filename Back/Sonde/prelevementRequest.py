import requests

baseUrl = "127.0.0.1:5000"

def send():
	r = requests.post(baseUrl + '/post', json={
  		"temperature": "Jason Sweet",
  		"Quantity": 1,
  		"Price": 18.00
	})
	print(f"Status Code: {r.status_code}, Response: {r.json()}")