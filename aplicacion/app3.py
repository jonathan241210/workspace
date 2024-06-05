import base64
import json
import requests

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read())
    return encoded_string.decode('utf-8')

# Ruta de la imagen que deseas convertir
image_path = '/workspace/workspace/1000031205.jpg'

# Llamada a la función y obtención del resultado
base64_string = image_to_base64(image_path)
"""print(base64_string)"""

url = 'http://localhost:11434/api/generate' 
data = {
  "model": "llava",
  "prompt":"What is in this picture?",
  "stream": False,
  "images": [base64_string]
  }

response = requests.post(url, json = data)
response = json.loads(response.text)

print(response['response'])