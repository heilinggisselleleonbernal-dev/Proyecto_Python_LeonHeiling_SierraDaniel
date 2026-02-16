import json

def cargar_grupos():
    with open("grupos.json", "r", encoding="utf-8") as archivo:
        grupos = json.load(archivo)
    return grupos

def guardar_grupos(grupos):
    with open("grupos.json", "w", encoding="utf-8") as archivo:
        json.dump(grupos, archivo, indent=4, ensure_ascii=False)

def cargar_campers():
    try:
        with open("campers.json", "r", encoding="utf-8") as archivo:
            campers = json.load(archivo)
    except FileNotFoundError:
        campers = []
    return campers

def guardar_campers(campers):
    with open("campers.json", "w", encoding="utf-8") as archivo:
        json.dump(campers, archivo, indent=4, ensure_ascii=False)

def menuTrainer(trainer):
    # Buscar el id del trainer por correo
    trainer_id = None
    try:
        with open("trainer.json", "r", encoding="utf-8") as archivo:
            trainers_data = json.load(archivo)
            trainers_list = trainers_data.get("lista_Trainers", [])
            for t in trainers_list:
                if t.get("correo") == trainer.get("correo"):
                    trainer_id = t.get("id")
                    break
    except Exception:
        pass

    while True:
        print("-----------------------------------------------")
        print("Que es lo que quieres hacer?")
        print("1. Ver grupos asignados y sus campers")
        print("2. Calificar modulos")
        print("3. Ver promedios de los modulos")
        print("4. Salir")
        print("-----------------------------------------------")
        opcion = input("Ingrese el numero de la opcion que desea: ")

        if opcion == "1":
            grupos= cargar_grupos()
            print("Grupos asignados:")
            for grupo in grupos:
                if ("trainer_id" in grupo and grupo["trainer_id"] == trainer_id) or ("trainerId" in grupo and grupo["trainerId"] == trainer_id):
                    print(f"Grupo: {grupo['idGrupo']}, Ruta: {grupo['ruta']}, Salon: {grupo['salon']}")
                    print("Campers asignados:")
                    for camper in grupo["campers"]:
                        nombre = camper.get("nombres") or camper.get("nombre") or ""
                        apellidos = camper.get("apellidos") or camper.get("apellido") or ""
                        print(f"- {nombre}, {apellidos}")
        
        elif opcion == "2":
            print("Seleccione el grupo para calificar:")
            