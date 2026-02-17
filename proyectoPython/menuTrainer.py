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
            grupos = cargar_grupos()
            grupo_seleccionado = input("Ingrese el grupo: ")
            for grupo in grupos:
                if grupo["idGrupo"] == grupo_seleccionado:
                    id_camper = input("Id del camper: ")
                    print("Modulos disponibles:")
                    for i, modulo in enumerate(grupo["modulos"], 1):
                        print(f"{i}- {modulo['nombre']}")
                    modulo_seleccionado = int(input("Seleccione el modulo a calificar: "))  
                    if modulo_seleccionado < 1 or modulo_seleccionado > len(grupo["modulos"]):
                        print("Modulo inválido ❌")
                        break
                    evaluacion_existente = None
                    for ev in modulo["evaluaciones"]:
                        if ev.get("idCamper") == id_camper: 
                            evaluacion_existente = ev
                            break
                    if evaluacion_existente:
                        print("El camper ya tiene una nota registrada.")
                        editar= input("¿Desea editar la nota?: ")
                        if editar.lower() != "si":
                            print("No se editó la nota.")
                            break
                        actividad = input(f"Actividad actual ({evaluacion_existente.get('actividad', '')}): ")
                        practica = input(f"Práctica actual ({evaluacion_existente.get('practica', '')}): ")
                        teorica = input(f"Teórica actual ({evaluacion_existente.get('teorica', '')}): ")
                        if actividad:
                            evaluacion_existente["actividad"] = float(actividad)
                        if practica:
                            evaluacion_existente["practica"] = float(practica)
                        if teorica:
                            evaluacion_existente["teorica"] = float(teorica)
                        notas = [evaluacion_existente.get("actividad"), evaluacion_existente.get("practica"), evaluacion_existente.get("teorica")]
                        if all(isinstance(n, (int, float)) for n in notas):
                            evaluacion_existente["definitiva"] = sum(notas) / 3
                            print(f"Definitiva calculada: {evaluacion_existente['definitiva']}")
                        else:
                            evaluacion_existente["definitiva"] = None
                        guardar_grupos(grupos)
                        print("Evaluación actualizada exitosamente.")
                    else:
                        actividad = float(input("Ingrese la calificación de la actividad: "))
                        practica = float(input("Ingrese la calificación de la práctica: "))
                        teorica = float(input("Ingrese la calificación teórica: "))
                        definitiva = ((actividad*0.1) + (practica*0.6) + (teorica*0.3))
                        if definitiva >= 60.0:
                            aprobado = True
                        else:
                            aprobado = False
                        evaluacion = {
                            "idCamper": id_camper,
                            "actividad": actividad,
                            "practica": practica,
                            "teorica": teorica,
                            "definitiva": definitiva,
                            "aprobado": aprobado
                        }
                        modulo["evaluaciones"].append(evaluacion)
                        print(f"Definitiva calculada: {definitiva}")
                        guardar_grupos(grupos)
                        print("Evaluación guardada exitosamente.")
                    break

        elif opcion == "3":
            grupos = cargar_grupos()
            grupo_seleccionado = input("Ingrese el grupo: ")
            for grupo in grupos:
                if grupo["idGrupo"] == grupo_seleccionado:
                    id_camper = input("Id del camper: ")
                    print("Modulos evaluados:")
                    for i, modulo in enumerate(grupo["modulos"], 1):
                        print(f"{i}- {modulo['nombre']}")
                    modulo_opcion = int(input("Seleccione el modulo para ver promedios: "))
                    modulo = grupo["modulos"][modulo_opcion - 1]
                    for nota in modulo["evaluaciones"]:
                        if nota.get("idCamper") == id_camper:
                            print(f"Definitiva del módulo {modulo['nombre']}: {nota.get('definitiva', 'No calculada')}")
                            break
                    else:
                        print(f"No se encontró evaluación para el camper en el módulo {modulo['nombre']}.")
                    break

        elif opcion == "4":
            print("Saliendo del programa...")
            break   


                                  
