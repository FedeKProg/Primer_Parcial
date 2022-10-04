'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones

url_archivo = r"C:\Users\Freelancer\Desktop\Parcial\PP_STARWARS\data.json"

def starwars_app():
    contenido = []
    lista_personajes = funciones.abrir_json(url_archivo)
    while(True):
        print("1 - Listar los personajes ordenados por altura\n"
            "2 - Mostrar el personaje mas alto de cada genero\n"
            "3 - Ordenar los personajes por peso\n"
            "4 - Armar un buscador de personajes\n"
            "5 - Exportar lista personajes a CSV\n"
            "6 - Salir\n\n")
        respuesta = input()
        if(respuesta=="1"):
            contenido = funciones.mostrar(funciones.orden_altura(lista_personajes))
        elif(respuesta=="2"):
            genero = input("Ingrese un genero para saber el personaje mas alto dentro del mismo (male, female, n/a)\n\n")
            if genero == "male":
                contenido = funciones.orden_altura_genero_m(lista_personajes,genero)
            elif genero == "female":
                contenido = funciones.orden_altura_genero_f(lista_personajes,genero)
            elif genero == "n/a":
                contenido = funciones.orden_altura_genero_na(lista_personajes,genero)
        elif(respuesta=="3"):
            contenido = funciones.mostrar(funciones.orden_peso(lista_personajes))
        elif(respuesta=="4"):
            key = input("Ingrese el nombre del personaje que desea buscar\n\n")
            contenido = funciones.buscador_personajes(lista_personajes,key)
        elif(respuesta=="5"):
            funciones.export_to_csv(str(contenido), "data_personajes.csv")
        elif(respuesta=="6"):
            break


starwars_app()

