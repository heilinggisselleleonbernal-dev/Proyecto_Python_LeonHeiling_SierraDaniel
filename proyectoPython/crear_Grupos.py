import json
import os
def crear_grupos():
    with open( os.path.join(os.path.dirname(__file__), "trainer.json")) as file:
        trainers = json.load(file)
    trainers_list = trainers["lista_Trainers"]
    with open( os.path.join(os.path.dirname(__file__), "grupos.json")) as file:
        grupos = json.load(file)
        print("Profesores disponibles:")
    for i in range(len(trainers_list)):
        print(i+1, ".", trainers_list[i]["nombre"],
              "Horario: ", trainers_list[i]["horaInicio"],
              "-", trainers_list[i]["horaFin"])    
    profe = int(input("Seleccione profesor: "))
    trainer = trainers_list[profe-1]     
    print("Bloques disponibles:")
    bloques = [] 
    inicio = trainer["horaInicio"]
    contador = 1                                            
    while inicio < trainer["horaFin"]:
        fin = inicio + 4
        ocupado = False
        for g in grupos:
            if g["trainerId"] == trainer["id"] and g["horaInicio"] == inicio:
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
    horaInicio = bloques[bloque_hora-1][0]  
    horaFin = bloques[bloque_hora-1][1]
    letra = trainer["nombre"][0].upper() 
    nombre_grupo = letra + str(bloque_hora)
    print("Rutas disponibles:") 
    for i in range(len(trainer["especialidad"])):
        print(i+1, ".", trainer["especialidad"][i])

    rutaOp = int(input("Seleccione ruta: "))
    ruta = trainer["especialidad"][rutaOp-1]    
    with open( os.path.join(os.path.dirname(__file__), "salones.json")) as file:
        salones = json.load(file)
    print("Salones disponibles:")
    for i in range(len(salones)):
        print(i+1, ".", salones[i]["nombre"], "Capacidad:", salones[i]["capacidad"])
    salonOp = int(input("Seleccione salón: ")) 
    salon = salones[salonOp-1]["nombre"]
    for g in grupos:
        if g["salon"] == salon and g["hora_inicio"] == horaInicio:
            print("El salón seleccionado no está disponible en el horario elegido.")
            return

    modulos = [
    {"nombre": "Fundamentos", "evaluaciones": []},
    {"nombre": "Web", "evaluaciones": []},
    {"nombre": "Bases de Datos", "evaluaciones": []}
    ]

    if ruta.upper() == "java":
        modulos.append({"nombre": "Backend Java", "evaluaciones": []})
    elif ruta.upper() == "nodejs":
        modulos.append({"nombre": "Backend NodeJs", "evaluaciones": []})
    elif ruta.upper() == "netcore":
        modulos.append({"nombre": "Backend NetCore", "evaluaciones": []})

    nuevoGrupo = {
        "idGrupo": nombre_grupo,
        "trainerId": trainer["id"],
        "ruta": ruta,
        "salon": salon,
        "horaInicio": horaInicio,
        "horaFin": horaFin,
        "estado": "Planeado",
        "campers": [],
        "modulos": modulos
        }       
    grupos.append(nuevoGrupo)     
    with open( os.path.join(os.path.dirname(__file__), "grupos.json"), "w") as file:
        json.dump(grupos, file, indent=4)   

    print("Grupo creado correctamente!")
    print("Nombre grupo:", nombre_grupo)
    print("Ruta:", ruta)
    print("Horario:", horaInicio, "-", horaFin)
    print("Salon:", salon)
    