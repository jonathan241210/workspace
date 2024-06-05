import base64
import json
import requests
import google.generativeai as genai
from IPython.display import display, Markdown
import pathlib
import textwrap

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read())
    return encoded_string.decode('utf-8')

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Ruta de la imagen que deseas convertir
image_path = '/workspace/workspace/1000031205.jpg'

# Llamada a la función y obtención del resultado
base64_string = image_to_base64(image_path)

# URL de la API local
url = 'http://localhost:11434/api/generate'

# Datos para la solicitud a la API local
data = {
    "model": "llava",
    "prompt": "What is in this picture?",
    "stream": False,
    "images": [base64_string]
}

# Realizar la solicitud a la API local
response = requests.post(url, json=data)
response_json = json.loads(response.text)

# Obtener la descripción de la imagen de la respuesta
image_description = response_json['response']

# Coloca tu clave API aquí
GOOGLE_API_KEY = 'AIzaSyDUBlBhv5G-kmNVsITZ7yHADxweVjop2ME'

# Autenticar usando la clave API
genai.configure(api_key=GOOGLE_API_KEY)

# Listar modelos disponibles y seleccionar el adecuado
model_name = None
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        model_name = m.name
        print(f'Model available for content generation: {model_name}')
        break

# Verificar si se encontró un modelo adecuado
if model_name:
    # Crear una instancia del modelo
    model = genai.GenerativeModel(model_name)
    
    # Generar contenido basado en la descripción de la imagen
    response = model.generate_content(image_description)
    
    # Mostrar la respuesta en formato Markdown
    display(to_markdown(response['content']))
else:
    print('No suitable model found for content generation.')
