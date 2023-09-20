import requests
import json
import pandas as pd

url = "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all"

respuesta = requests.get(url)

# estoy teniendo problemas para levantar la api por lo tanto agrego una verificacion para ver que pasa

if respuesta.status_code == 200:
    try:
        datosperros= respuesta.json()
        if datosperros:
            facto_perro= data[0]["fact"]
            dfperros = pd.DataFrame({"facto": [facto_perro]})
            print(dfperros.head())
        else:
            print("Respuesta esta vacia")
    except json.JSONDecodeError as e:
        print("Error en el JSON", str(e))
else:
    print("El error esta en la API .Codigo:", respuesta.status_code)
