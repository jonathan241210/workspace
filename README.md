# workspace
# Llm
## paso 1 DESCARGARLO
descargar
curl -fsSL https://ollama.com/install.sh | sh

### paso 2 abrir el server
ollama serve

### Ejecutarlo en bash
ollama pull tinyllama

### Para preguntar
ollama run tinyllama ....
ollama run llava

### Modo Chat/Detener chat

ollama run tinyllama
detener: ctrl+D

### Los token
curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt":"¿Por qué el cielo es azul?",
  "stream": false
}'

### Pagina requests module
https://www.w3schools.com/python/module_requests.asp 

## comandos terminal
1.- git add .(guardar cualquier archivo que encuentre)
2.-git commit -m "UPDATED README"(poner un titulo al todos los cambios que hicimos)
3.-git push -u origin main(empuja nuestro codigo de nuestra maquina a github)