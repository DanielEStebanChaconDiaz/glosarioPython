import os

def asignarCampersASalones():
    def mostrar_archivos_disponibles():
        # Obtener la lista de archivos JSON en el directorio "module/storage/salones"
        archivos_json = [archivo for archivo in os.listdir("module/storage/salones") if archivo.endswith(".json")]
        
        # Imprimir los archivos disponibles para agregar campers
        print("Archivos JSON disponibles para agregar campers:")
        for i, archivo in enumerate(archivos_json, 1):
            print(f"{i}. {archivo}")
        
        return archivos_json  # Devolver la lista de archivos disponibles

    # Llamar a la función interna para mostrar los archivos disponibles
    archivos_disponibles = mostrar_archivos_disponibles()

# Llamar a la función externa para iniciar el proceso de asignación de campers a salones
asignarCampersASalones()


def cargar_campers_disponibles():
    try:
        # Intenta abrir el archivo "camper.json" en modo de lectura
        with open("module/storage/camper.json", "r") as f:
            # Carga los datos del archivo JSON en la variable campers
            campers = json.load(f)
    except FileNotFoundError:
        # Si el archivo no se encuentra, asigna una lista vacía a campers
        campers = []
        #AL MOMENTO DE HACERLO PORFAVOR DANIEL, CAMBIE LA LISTA POR UN PRINT QUE DIGA ERROR O ALGUNA VAINA, PQ SINO LE GENERA UN BUCLE INFINITO
    # Retorna la lista de campers cargada desde el archivo JSON o una lista vacía si el archivo no existe
    return campers

def seleccionar_archivo_json(archivos_json):
    """
    Esta función solicita al usuario que seleccione un archivo JSON de una lista de archivos disponibles.

    Args:
    - archivos_json (list): Una lista de nombres de archivos JSON disponibles.

    Returns:
    - str: El nombre del archivo JSON seleccionado por el usuario.
    """
    while True:
        try:
            seleccion = int(input("Seleccione el número del archivo JSON al que desea agregar campers: "))
            archivo_seleccionado = archivos_json[seleccion - 1]
            return archivo_seleccionado
        except (ValueError, IndexError):
            print("Número de archivo inválido. Inténtelo de nuevo.")

# Ejemplo de uso:
archivos_disponibles = ["archivo1.json", "archivo2.json", "archivo3.json"]
archivo_seleccionado = seleccionar_archivo_json(archivos_disponibles)
print(f"El archivo seleccionado es: {archivo_seleccionado}")

def seleccionar_camper(campers):
    """
    Esta función muestra una lista de campers disponibles y solicita al usuario que seleccione uno.

    Args:
    - campers (list): Una lista de diccionarios que representan los campers disponibles.

    Returns:
    - dict: El camper seleccionado por el usuario.
    """
    # Mostrar la lista de campers disponibles
    print("Campers disponibles:")
    for i, camper in enumerate(campers, 1):
        print(f"{i}. {camper['Nombre']} {camper['Apellido']}")
    
    # Solicitar al usuario que seleccione un camper
    while True:
        try:
            seleccion = int(input("Seleccione el número del camper que desea agregar al archivo JSON: "))
            camper_seleccionado = campers[seleccion - 1]
            return camper_seleccionado
        except (ValueError, IndexError):
            print("Número de camper inválido. Inténtelo de nuevo.")

# Ejemplo de uso:
campers_disponibles = [
    {"Nombre": "Juan", "Apellido": "Perez"},
    {"Nombre": "Maria", "Apellido": "Gonzalez"},
    {"Nombre": "Carlos", "Apellido": "Martinez"}
]
camper_seleccionado = seleccionar_camper(campers_disponibles)
print(f"El camper seleccionado es: {camper_seleccionado}")

def searchArtemis():
    # Abrir y cargar el archivo JSON
    with open ("module/storage/salones/sputnik.json") as f:
        sputnikdata = json.load(f)
    
    # Iterar sobre cada camper
    for camper in sputnikdata:
        # Mostrar información detallada del camper
        print(f"""
______________________
    Nombre: {camper['Nombre']}
    Apellido: {camper['Apellido']} 
    Edad: {camper['Edad']}
    Género: {camper['Genero']}
    Teléfono: {camper['Telefono']}
    Horario: {camper['Horario']}
    Código de Ruta: {camper['codigoRuta']}
______________________
                """)
    
    # Mensaje de confirmación
    return "Estos son los campers encontrados en la ruta Artemis"
