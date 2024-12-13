# Detect time response in web server
import requests
import time

url = "http://example.com/login"
data = {"username": "admin", "password": "test123"}

start_time = time.time()
response = requests.post(url, data=data)
end_time = time.time()

print(f"Tiempo de respuesta: {end_time - start_time} segundos")
# En este script, envías una solicitud a un servidor web y mides cuánto tiempo tarda en responder.
# (Cambia los datos del formulario ligeramente para observar si los tiempos de respuesta cambian.)
