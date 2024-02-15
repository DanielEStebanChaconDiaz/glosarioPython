def delete():
    bandera = True
    while bandera:
        # Mostrar la lista de lista disponibles
        print("Lista de lista:")
        for i, val in enumerate(lista):
            print(f"""
            ________________
            Codigo: {val.get("codigo")}
            Nombre: {val.get("nombre_lista")}
            Modulo: {val.get("modulo")}
            ________________
            """)

        codigo = input("Ingrese el código de la lista que desea eliminar:\n")

        # Buscar la lista con el código ingresado
        lista_encontrada = None
        for lista in listas:
            if lista["codigo"] == codigo:
                lista_encontrada = lista
                break

        if lista_encontrada:
            print(f"""
            ________________
            Codigo: {lista_encontrada.get("codigo")}
            Nombre: {lista_encontrada.get("nombre_lista")}
            Modulo: {lista_encontrada.get("modulo")}
            ________________
            """)
            # Confirmar si desea eliminar la lista
            print("¿Este es la lista que desea eliminar?")
            print("1. Si")
            print("2. No")
            print("3. Salir")
            opc = int(input())
            if opc == 1:
                listas.pop(codigo)
                with open("module/storage/listas.json", "w") as f:
                    data = json.dumps(listas, indent=4)
                    f.write(data)
                bandera = False
            elif opc == 3:
                system("clear")
                bandera = False
        else:
            print("No se encontró ninguna lista con el código ingresado.")
            print("Por favor, inténtelo de nuevo.")

    return "lista eliminada"






def agregar_modulo():
    # Se crea un diccionario para almacenar la información del nuevo módulo
    modulo = {
        "codigo": input("Ingrese el codigo:\n"),  # Se solicita al usuario que ingrese el código del módulo
        "nombre_modulo": input("Ingrese el nombre del módulo:\n"),  # Se solicita al usuario que ingrese el nombre del módulo
        "agregar datos adicionales": [],  # Se inicializa una lista vacía para almacenar datos adicionales del módulo
    }
    
    # Se pregunta al usuario cuántos temas desea ingresar para el módulo
    cantidad_datos = int(input("¿Cuántos datos adicionales desea ingresar?\n"))
    
    # Se itera sobre la cantidad de temas ingresados por el usuario
    for i in range(1, cantidad_datos + 1):
        # Se solicita al usuario que ingrese el nombre del dato adicional y se agrega a la lista de datos adicionales del módulo
        dato_Adicional = input(f"Ingrese el dato adicional #{i} del módulo:\n")
        modulo["agregar datos adicionales"].append(dato_Adicional)
    
    try:
        # Se intenta abrir el archivo "modulos.json" en modo lectura
        with open("module/storage/modulos.json", "r") as file:
            # Se carga el contenido del archivo JSON en la lista modulos
            modulos = json.load(file)
    except FileNotFoundError:
        # Si el archivo no existe, se inicializa una lista vacía
        modulos = []
    
    # Se agrega el nuevo módulo a la lista de módulos
    modulos.append(modulo)
    
    # Se abre el archivo "modulos.json" en modo escritura
    with open("module/storage/modulos.json", "w") as file:
        # Se escribe la lista de módulos actualizada en formato JSON con una sangría de 4 espacios
        json.dump(modulos, file, indent=4)











#Esto para asignacion de algo
# Se crea un diccionario con los datos de la nueva lista
nombre_diccionario = {
    "codigo": f"R{len(listta)+1}",  # Se genera un código único para la lista
    "nombre_lista": input("Ingrese el nombre de la lista:\n "),
    "agregar_modulo": asignarModulos()  # Se llama a la función asignarModulos() para seleccionar los módulos de la lista
}

# Se agrega la nueva lista a la lista de listas
lista.append(nombre_diccionario)

# Se define la lista del archivo "listas.json"
path = "module/storage/"

# Se abre el archivo "listas.json" en modo escritura y se guarda la lista de listas como JSON
with open(path + "listas.json", "w") as f:
    f.write(json.dumps(lista, indent=4))  # Se escribe la lista de lista en formato JSON
    f.close()  # Se cierra el archivo
