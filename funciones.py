import json
import re
from subprocess import list2cmdline

'''
{
			"name": "Luke Skywalker",
			"height": "172",
			"mass": "77",
			"gender": "male"
		},
'''

url_archivo = r"C:\Users\Freelancer\Desktop\Parcial\PP_STARWARS\data.json"

def abrir_json(path:str)->list:
    with open(path, "r") as file:
        data_personajes = json.load(file)
    return data_personajes["results"]

lista_personajes = abrir_json(url_archivo)


def buscar_maximo(lista_personajes:list,clave:str)->int:
    maximo = 0
    for i in range(len(lista_personajes)):
        if lista_personajes[i][clave] > lista_personajes[maximo][clave]:
            maximo = i
    return maximo

# def buscar_maximo_genero(lista_personajes:list,clave:str)->int:
#     maximo = 0
#     for i in range(len(lista_personajes)):
#         if lista_personajes[i][clave] > lista_personajes[maximo][clave]:
#             maximo = i
#     return maximo

def orden_altura (lista_personajes:list)->list:
    copia_lista = lista_personajes.copy()
    lista_altura_ordenada = []

    while len(copia_lista) > 0:
            maximo = buscar_maximo(copia_lista,"height")
            lista_altura_ordenada.append(copia_lista.pop(maximo))
    for personaje in lista_altura_ordenada:
        print(personaje["name"], personaje["height"], "cm")
    return lista_altura_ordenada

#orden_altura(lista_personajes)

def orden_altura_genero_m(lista_personajes:list,genero:str)->list:
    copia_lista = lista_personajes.copy()
    personaje_alto = copia_lista[0]
    for personaje in copia_lista:
        if personaje["gender"] == "male" and personaje["height"] >= personaje_alto["height"]:
            personaje_alto = personaje
            print("El personaje maculino mas alto es {0} con una altura de {1} cm".format(personaje["name"], personaje["height"]))
def orden_altura_genero_f(lista_personajes:list,genero:str)->list:
    copia_lista = lista_personajes.copy()
    personaje_alto = copia_lista[0]
    for personaje in copia_lista:
        if personaje["gender"] == "female" and personaje["height"] >= personaje_alto["height"]:
            personaje_alto
            print("El personaje femenino mas alto es {0} con una altura de {1} cm".format(personaje["name"], personaje["height"]))
def orden_altura_genero_na(lista_personajes:list,genero:str)->list:
    copia_lista = lista_personajes.copy()
    personaje_alto = copia_lista[0]
    for personaje in copia_lista:
        if personaje["gender"] == "n/a" and personaje["height"] >= personaje_alto["height"]:
            personaje_alto = personaje
            print("El personaje sin genero mas alto es {0} con una altura de {1} cm".format(personaje["name"], personaje["height"]))

def orden_peso(lista_personajes:list)->list:
    copia_lista = lista_personajes.copy()
    lista_peso_ordenada = []

    while len(copia_lista) > 0:
        maximo = buscar_maximo(copia_lista,"mass")
        lista_peso_ordenada.append(copia_lista.pop(maximo))
    for personaje in lista_peso_ordenada:
        print(personaje["name"], personaje["mass"], "kg")
    return lista_peso_ordenada
#orden_peso(lista_personajes)

def buscador_personajes(lista_personajes:list,key:str)->list:
    for personaje in lista_personajes:
        if re.search(key,personaje["name"],re.IGNORECASE):
            print("{0} - {1}".format(personaje["name"], personaje["gender"]))
    return
#buscador_personajes(lista_personajes,"r")

def mostrar(lista_personajes:list):
    mensaje = ""
    
    for personaje in lista_personajes:
        mensaje += "{0}, {1}, {2}, {3}\n".format(personaje["name"],personaje["height"], personaje["mass"], personaje["gender"])
    return mensaje

def export_to_csv(mensaje:str,nombre_csv:str):
    nombre_csv = "data_personajes.csv"
    with open(nombre_csv, "w") as file:
        file.write(mensaje)