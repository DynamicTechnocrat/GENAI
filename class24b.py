import requests

url = " http://127.0.0.1:5000/watai"

details = {"name" : "daniel" , "message" : "what is the update  "}

result = requests.post(url , json = details)

print(result.text)

