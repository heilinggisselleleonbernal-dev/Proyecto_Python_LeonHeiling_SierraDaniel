import json
import os

def menu_Coordinador():
    while True:
        print("1.gestiona campers")
        print("2.gestiona trainers")
        print("3.salir")
        opcion_raw = input("seleccione:")
        try:
            opcion = int(opcion_raw)
        except ValueError:
            print("Entrada inválida, ingrese un número.")
            continue
        if opcion == 1:
            print("----CAMPERS-----")
            print("1.listar campers")
            print("2.editar campers")
            print("3.volver")
            subopcion_raw = input("seleccione: ")
            try:
                subopcion = int(subopcion_raw)
            except ValueError:
                print("Entrada inválida, ingrese un número.")
                continue
            if subopcion == 1:
                try:
                    ruta = os.path.join(os.path.dirname(__file__), "campers.json")
                    with open(ruta, "r", encoding="utf-8") as archivo:
                        datos = json.load(archivo)
                        campers = datos.get("lista_Campers", [])
                    if not campers:
                        print("No hay campers registrados")
                    else:
                        for camper in campers:
                            print("ID:", camper["identificacion"])
                            print("Nombre:", camper["nombres"], camper["apellidos"])
                            print("Estado:", camper["estado"])
                except FileNotFoundError:
                    print(f"No existe el archivo de campers: {ruta}")
                except json.JSONDecodeError:
                    print(f"El archivo {ruta} contiene JSON inválido")
            if subopcion == 2:
                print("-")

        elif opcion == 2:
            print("1.añadir trainers")
            print("2.editar trainers")
            print("1.listar trainers")
            print("4.eliminar trainers")





