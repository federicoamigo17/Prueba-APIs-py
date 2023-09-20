import requests
import json
import pandas as pd

url = "https://pokeapi.co/api/v2/pokemon?limit=10&offset=10"

try:
    respuesta = requests.get(url)
    respuesta.raise_for_status()  # Lanza una excepción para códigos de error HTTP
    respuestajson = respuesta.json()
    df = pd.DataFrame(respuestajson["results"])
    dflimpio = df[["name", "url"]]
    print(dflimpio)
except requests.exceptions.RequestException as e:
    print("Error al hacer la solicitud:", e)
except json.JSONDecodeError as e:
    print("Error al decodificar JSON:", e)
except KeyError as e:
    print("Error de clave:", e)


  