#primero que todo se importan los json y luego se importan los modulos
import json
from os import system
import json
from .validate import menuNoValid  # Se asume la existencia de un módulo validate
from .data import camper, genero, discapacidad, estado, rutas  # Se asume la existencia de un módulo data
from .archivo_De_donde_Se_importara import nombre_De_la_variable
def menu():
    #Aqui definimos la funcion a la cual entraremos desde el main
    #ahora lo que haremos es la salida por consola 
    #para que el usuario sepa a donde entrara
    print("""CRUD (nombre del menu)
          1. primera op
          2. segunda op
          3. tercera op
          etc
          """)
    #una vez teniendo el menu, lo que haremos sera 
    #sacar la entrada por consola
    opc = int(input())
    #para que la entrada por consola funcione hay que hacer los casos
    match opc:
        case 1:
            #aqui tenemos un caso, y dentro de el podemos hacer 2 cosas
            #poner una funcion, para acceder al contenido de la misma
            def caulquier_def_que_se_necesite():
                pass

def save():
    # Sección para guardar la información de un nuevo camper
    pass

def edit():
    # Sección para editar la información de un camper existente
    pass

def search():
    # Sección para buscar y visualizar la información de los campers registrados
    pass

def delete():
    # Sección para eliminar un camper del sistema
    pass

def modulos():
    # Sección para asignar un camper a una ruta existente
    pass

def menu():
    # Menú principal para interactuar con el módulo de campers
    pass

# Llamada a la función de menú para iniciar la ejecución del programa
menu()
