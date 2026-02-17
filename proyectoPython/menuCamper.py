import json

def cargar_grupos():
    try:
        with open("grupos.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_grupos(grupos):
    with open("grupos.json", "w", encoding="utf-8") as archivo:
        json.dump(grupos, archivo, indent=4, ensure_ascii=False)

def cargar_campers():
    try:
        with open("campers.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return datos.get("lista_Campers", [])
    except FileNotFoundError:
        return []

def guardar_campers(campers):
    with open("campers.json", "w", encoding="utf-8") as archivo:
        json.dump({"lista_Campers": campers}, archivo, indent=4, ensure_ascii=False)


def menuCamper():
    while True:
        print("-----------------------------------------------")
        print("Que es lo que quieres hacer?")
        print("1. ver datos personales")
        print("2. ver grupos asignados y sus campers")
        print("3. ver notas de cada modulo")
        print("4. Revisar Estado")
        print("5. Salir")
        print("-----------------------------------------------")
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            campers = cargar_campers()
            print("Tus datos personales:")
            for camper in campers:
                print(f"Nombre: {camper['nombres']} {camper['apellidos']}")
                print(f"Identificación: {camper['identificacion']}")
                print(f"Correo: {camper.get('correo', 'No disponible')}")
                print(f"Teléfono: {camper.get('telefono', 'No disponible')}")
                print(f"Estado: {camper.get('estado', 'No disponible')}")
                print(f"Riesgo: {camper.get('riesgo', 'No disponible')}")
                print("-----------------------------------------------")

        elif opcion == "2":
            grupos = cargar_grupos()
            print("Grupos asignados:")
            for grupo in grupos:
                print(f"Grupo: {grupo['idGrupo']}, Ruta: {grupo['ruta']}, Salon: {grupo['salon']}")
                print("Campers asignados:")
                for camper in grupo["campers"]:
                    nombre = camper.get("nombres") or camper.get("nombre") or ""
                    apellidos = camper.get("apellidos") or camper.get("apellido") or ""
                    print(f"- {nombre}, {apellidos}")

        elif opcion == "3":
            grupos = cargar_grupos()
            id_camper = input("Ingrese su identificación: ")
            print("Modulos evaluados:")
            for grupo in grupos:
                for modulo in grupo["modulos"]:
                    for evaluacion in modulo["evaluaciones"]:
                        if evaluacion.get("idCamper") == id_camper:
                            print(f"Modulo: {modulo['nombre']}")
                            print(f"Definitiva: {evaluacion.get('definitiva', 'No disponible')}")

        elif opcion == "4":
            campers = cargar_campers()
            id_camper = input("Ingrese su identificación: ")
            for camper in campers:
                if camper["identificacion"] == id_camper:
                    print(f"Estado: {camper.get('estado', 'No disponible')}")
                    print(f"Riesgo: {camper.get('riesgo', 'No disponible')}")

        elif opcion == "5":
            print("Saliendo del menú...")
            break