import google.generativeai as genai
from IPython.display import display, Markdown
import textwrap

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

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
    
    # Generar contenido
    response = model.generate_content("What is the meaning of life?")
    
    # Mostrar la respuesta en formato Markdown
    display(to_markdown(response['content']))
else:
    print('No suitable model found for content generation.')

