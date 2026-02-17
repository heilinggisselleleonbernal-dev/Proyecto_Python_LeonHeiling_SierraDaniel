import json
import os

def crear_grupos():

    with open(os.path.join(os.path.dirname(__file__), "trainer.json")) as file:
        trainers = json.load(file)

    trainers_list = trainers["lista_Trainers"]

    with open(os.path.join(os.path.dirname(__file__), "grupos.json")) as file:
        grupos = json.load(file)

    print("Profesores disponibles:")

    for i in range(len(trainers_list)):
        print(
            i + 1, ".", trainers_list[i]["nombre"],
            "Horario:", trainers_list[i]["horaInicio"],
            "-", trainers_list[i]["horaFin"] 
        )

    profe = int(input("Seleccione profesor: "))
    trainer = trainers_list[profe - 1]

    print("Bloques disponibles:")

    bloques = []
    inicio = int(trainer["horaInicio"][:2])
    fin_hora = int(trainer["horaFin"][:2])
    contador = 1

    while inicio < fin_hora:

        fin = inicio + 4
        ocupado = False

        for g in grupos:
            grupo_hora = g["horaInicio"]
            if isinstance(grupo_hora, str):
                grupo_hora_int = int(str(grupo_hora)[:2])
            else:
                grupo_hora_int = int(grupo_hora)
            if g.get("trainerId", g.get("trainer_id")) == trainer["id"] and grupo_hora_int == inicio:
                ocupado = True
                break

        if not ocupado:
            print(contador, ".", inicio, "-", fin)
            bloques.append((inicio, fin))
        else:
            print(contador, ".", inicio, "-", fin, "(ocupado)")

        inicio += 4
        contador += 1

    if len(bloques) == 0:  
        print("Este profesor no tiene horarios disponibles.")
        return

    bloque_hora = int(input("Seleccione bloque disponible: "))

    if bloque_hora < 1 or bloque_hora > len(bloques):
        print("Bloque inválido.")
        return

    horaInicio = bloques[bloque_hora - 1][0]
    horaFin = bloques[bloque_hora - 1][1]

    letra = trainer["nombre"][0].upper()
    nombre_grupo = letra + str(bloque_hora)

    print("Rutas disponibles:")

    for i in range(len(trainer["especialidad"])):
        print(i + 1, ".", trainer["especialidad"][i])

    rutaOp = int(input("Seleccione ruta: "))

    if rutaOp < 1 or rutaOp > len(trainer["especialidad"]): 
        print("Ruta inválida.")
        return

    ruta = trainer["especialidad"][rutaOp - 1]

    with open(os.path.join(os.path.dirname(__file__), "salones.json")) as file:
        salones = json.load(file)

    print("Salones disponibles:")

    for i in range(len(salones)):
        print(i + 1, ".", salones[i]["nombre"], "Capacidad:", salones[i]["capacidad"])

    salonOp = int(input("Seleccione salón: "))

    if salonOp < 1 or salonOp > len(salones):  
        print("Salón inválido.")
        return

    salon = salones[salonOp - 1]["nombre"]

    for g in grupos:
        if g["salon"] == salon and g["horaInicio"] == horaInicio: 
            print("El salón seleccionado no está disponible en el horario elegido.")
            return

    modulos = [
        {"nombre": "Fundamentos", "evaluaciones": []},
        {"nombre": "Web", "evaluaciones": []},
        {"nombre": "Bases de Datos", "evaluaciones": []}
    ]

    if ruta.upper() == "JAVA":
        modulos.append({"nombre": "Backend Java", "evaluaciones": []})
    elif ruta.upper() == "NODEJS":
        modulos.append({"nombre": "Backend NodeJs", "evaluaciones": []})
    elif ruta.upper() == "NETCORE":
        modulos.append({"nombre": "Backend NetCore", "evaluaciones": []})

    with open(os.path.join(os.path.dirname(__file__), "campers.json")) as file:
        campers_data = json.load(file)

    campers_list = campers_data["lista_Campers"]

    print("Campers disponibles:")

    for i, camper in enumerate(campers_list, 1):
        print(f"{i}. {camper['nombres']} {camper['apellidos']} (ID: {camper['identificacion']})")

    seleccionados = input("Ingrese los números de los campers separados por coma: ")
    seleccionados = [int(x.strip()) for x in seleccionados.split(",") if x.strip().isdigit()]

    campers_grupo = []

    for idx in seleccionados:
        if 1 <= idx <= len(campers_list):
            camper = campers_list[idx - 1]

            campers_grupo.append({
                "identificacion": camper["identificacion"],
                "nombre": camper["nombres"],
                "apellidos": camper["apellidos"],
                "correo": camper.get("correo", "")
            })

    for modulo in modulos:
        for camper in campers_grupo:
            modulo["evaluaciones"].append({
                "idCamper": camper["identificacion"],
                "actividad": "",
                "practica": "",
                "teorica": "",
                "definitiva": ""
            })

    nuevoGrupo = {
        "idGrupo": nombre_grupo,
        "trainerId": trainer["id"],
        "ruta": ruta,
        "salon": salon,
        "horaInicio": horaInicio,
        "horaFin": horaFin,
        "estado": "Planeado",
        "campers": campers_grupo,
        "modulos": modulos
    }

    grupos.append(nuevoGrupo)

    with open(os.path.join(os.path.dirname(__file__), "grupos.json"), "w") as file:
        json.dump(grupos, file, indent=4)

    print("Grupo creado correctamente!")
    print("Nombre grupo:", nombre_grupo)
    print("Ruta:", ruta)
    print("Horario:", horaInicio, "-", horaFin)
    print("Salon:", salon)
