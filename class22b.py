import requests

url = "http://127.0.0.1:5000/greeting"

details = {"age":45,"city":"lagos"}

response = requests.post(url , json = details) 
print(response.text)

### Generative ai 