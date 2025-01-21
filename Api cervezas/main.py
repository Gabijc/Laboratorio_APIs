# En este archivo encontraremos el código utilizado para realizar las requests y para trabajar con la API de cervezas de EEUU.

# Ejercicio propuesto:
# 1. Realiza una solicitud para obtener cervecerías por tipo (`micro`) en California.
# 2. Organiza la información en un DataFrame.
# 3. Calcula cuántas cervecerías hay por ciudad en California.
# 4. Crea un gráfico de barras que muestre las ciudades con más cervecerías.
 
# Importamos las líbrerias
import pandas as pd # type: ignore
import numpy as np # type: ignore
import requests # type: ignore # nos permite hacer peticiones HTTP fácilmente.
from tqdm import tqdm # type: ignore # Tqdm es una biblioteca de Python que proporciona barras de progreso rápidas y extensibles para bucles e iterables
import os # importación del entorno
from dotenv import load_dotenv # type: ignore # sirve para importar la variable de entorno
import seaborn as sns
import matplotlib.pyplot as plt

# Cargamos las variables de entorno, es decir, cargamos las variables que hemos creado en el entorno. En este caso es solo la key de la API
load_dotenv()
url_api = os.getenv("URL_API")

# Verificamos la clave API
if not url_api:
    raise ValueError("La URL API no se encuentra en el archivo .env")

response = requests.get(url_api)

data = response.json()

cervecerias_lista = {
    "nombre": [],
    "tipo": [],
    "ciudad": [],
    "estado": [],
    "direccion": []
}

def micro_cervecerias(datos, lista):
    """ Función que crea indica el número total de cervecerías de tipo micro que hay en California.

    Args:
        datos (json): datos sobre las cervecerías de EEUU.
        lista (list): lista con las cervecerías de EEUU.

    Returns:
        str: Frase que indica el número total de cervecerías de tipo micro en California.
    """

    pd.set_option('display.max_columns', None)

    for brewery in datos:
        if brewery['brewery_type'] == 'micro' and brewery['state'] == 'California':
            lista["nombre"].append(brewery['name'])
            lista["tipo"].append(brewery['brewery_type'])
            lista["ciudad"].append(brewery['city'])
            lista["estado"].append(brewery['state'])
            lista["direccion"].append(brewery['address_1'])

    dataframe_cervcerias_micro = pd.DataFrame(cervecerias)
    print(f"En California hay {dataframe_cervcerias_micro["ciudad"].count()} de tipo micro")
    return dataframe_cervcerias_micro
    
def cervecerias(datos, lista):
    """Función que crea un gráfico con las tres ciudades con más cervecerías de EEUU.

    Args:
        datos (json): Datos sobre todas las cervecerías de EEUU.
        lista (list): Lista que contiene las cervecerías de EEUU.

    Returns:
        Gráfico: gráfico con las tres ciudades con más cervecerías de EEUU.
    """

    pd.set_option('display.max_columns', None)

    for brewery in datos: 
        lista["nombre"].append(brewery['name'])
        lista["tipo"].append(brewery['brewery_type'])
        lista["ciudad"].append(brewery['city'])
        lista["estado"].append(brewery['state'])
        lista["direccion"].append(brewery['address_1'])

    dataframe_cervcerias = pd.DataFrame(lista)
    numero_cerv_ciudad = pd.DataFrame(dataframe_cervcerias["ciudad"].value_counts()).reset_index()
    
    sns.barplot(x="ciudad", y="count", data=numero_cerv_ciudad[:3])    
    plt.title("Ciudades de EEUU con más cervececías")
    plt.ylabel("Nº cervecerías")
    plt.xlabel("Ciudad")
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["top"].set_visible(False)
    plt.show()
    #print(numero_cerv_ciudad)        
    return dataframe_cervcerias


if __name__ == "__main__":
    #micro_cervecerias(data, cervecerias)
    cervecerias(data, cervecerias_lista)


