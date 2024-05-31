import requests
import json

uri = 'http://localhost:11434/api/generate'
myobj = {
  "model": "tinyllama",
  "prompt":"por que el cielo es azul?",
  "stream": False
  
}

response = requests.post(uri, json = myobj)
response = json.loads(response.text)


print(response['response'])