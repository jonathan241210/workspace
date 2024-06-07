import requests
import json

uri = "https://api.groq.com/openai/v1/chat/completions"

API_KEY='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'
headers={
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

data = {
         "messages": [
           {
             "role": "system",
             "content": "eres papa pitufo y respondes las preguntas con codigo de alta calida y una explicacion de cada linea de codigo"
           },
           {
             "role": "user",
             "content": "ejemplo de la libreria requests en python\n"
           }
           
         ],
         "model": "llama3-8b-8192",
         "temperature": 0.7,
         "max_tokens": 1024,
         "top_p": 1,
         "stream": False,
         "stop": None
        }
    

response = requests.post(uri, json = data, headers=headers)
response = json.loads(response.text)

print(response)