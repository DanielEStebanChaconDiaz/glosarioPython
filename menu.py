#primero que todo se importan los json y los modulos que deseemos agregar
#IMPORTANTE
#NO SE PUEDE PONER MAS DE UNA FUNCION EN MEIN
import json
import nombre_carpeta.nombre_modulo as nombre_modulo_importado

#se define menu
def menu():
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
            #poner para abrir un json y que nos mueva a un submenu
            #en este caso haremos la mas compleja
            with open("ruta de destino del json", "acompañado de (r) para leer") as f:
                #se usa as para renombrar lo del parentesis y hacerlo mas facil
                #ahora se pone el nombre del modulo importado y el nombre del archivo del modulo
                nombre_modulo_importado.nombre_modulo = json.loads
                #si no sale en verde el nombre_modulo_importado es pq lo hizo mal
                nombre_modulo_importado.def a la cual se quiere viajar()
                #ahora se pone la definicion a la cual se quiere viajar (debe estar en el modulo para que funcione)
                #y el json debe tener [] para que funcione

