import requests
import json
uri = "http://localhost:11434/api/generate -d" 
myobj ={
  "model": "llava",
  "prompt":"What is in this picture?",
  "stream": False,
  "images": []
}

response = requests.post(uri, json = myobj)
response = json.loads(response.text)


print(response['response'])