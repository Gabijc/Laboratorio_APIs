# Ejercicio Propuesto
# Realiza una búsqueda por palabra clave (s) para encontrar películas relacionadas con "Batman".
# Extrae las calificaciones de todas las películas encontradas.
# Calcula la calificación promedio de las películas en IMDb.
# Crea un gráfico de barras con las calificaciones obtenidas.

import os
from dotenv import load_dotenv # type: ignore
import requests # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore


load_dotenv()
api_key = os.getenv("API_KEY")
base_url = f"http://www.omdbapi.com/?"
titulo = "Batman"

def peli(url, key, ID):

    parametros = { "apikey": key, "i": ID}

    response = requests.get(url, params = parametros)
    datos = response.json()

    if response.status_code == 200:
        ...
    else:
        print(f"Error: {response.status_code}")
    # print(datos)
    return datos



def pelis_batman(url, key, titulo):
    
    parametros = { "apikey": key, "s": titulo}

    response = requests.get(url, params = parametros)

    if response.status_code == 200:
        print("Solicitud exitosa")
    else:
        print(f"Error: {response.status_code}")

    datos_batman = response.json()
    #print(datos)
    
    lista_datos_batman = {
        "titulo": [],
        "año lanzamiento": [],
        "tipo": [],
        "IMDBId": []}
    
    if "Search" in datos_batman:
        for dato in datos_batman["Search"]:
            lista_datos_batman["titulo"].append(dato["Title"])
            lista_datos_batman["año lanzamiento"].append(dato["Year"])
            lista_datos_batman["tipo"].append(dato["Type"])
            lista_datos_batman["IMDBId"].append(dato["imdbID"])

    pd.set_option('display.max_columns', None)
    datos_batman = pd.DataFrame(lista_datos_batman)

    ratings_batman ={
        "titulo": [],
        "rating": [],
        }

    for i in datos_batman["IMDBId"]:
        batman = peli(base_url, api_key, i)

        ratings_batman["titulo"].append(batman["Title"])
        ratings_batman["rating"].append(batman["imdbRating"])
        # rating = batman["Ratings"]
        #print(title)
        #print(rating)
        #print(rating_imdb)
        
    df_rating = pd.DataFrame(ratings_batman)
    df_batman = datos_batman.merge(right = df_rating, how = "left", on = "titulo")
    df_batman["rating"] = df_batman["rating"].astype(float)
    media = round(np.mean(df_batman["rating"]), 2)
    print(f"La calificacion media de las peliculas de Batman, según el IMDB Rating es: {media}")
    

    sns.barplot(x ="titulo", y ="rating", data = df_batman)
    plt.xticks(rotation = 20, ha="right", fontsize=8)
    plt.title("IMDB Rating Batman Movies")
    plt.ylabel("Rating")
    plt.xlabel("Titulo")

    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["top"].set_visible(False)

    plt.show()

if "__main__" == __name__:
    pelis_batman(base_url, api_key, titulo) 


        
#print(datos_batman)

    


# SOlicitud de un titulo en concreto: http://www.omdbapi.com/?apikey=[yourkey]&t=[titulo]