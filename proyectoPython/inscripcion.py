import json
import os

def proceso_inscripcion():
    print("Bienvenido a Campusland")

    nuevoIdentificacion=input("Numero de identificacion: ")
    nuevoNombre=input("Nombres: ")
    nuevoApellido=input("Apellidos: ")
    nuevoDireccion=input("Direccion: ")
    nuevoAcudiente=input("Nombre del acudiente: ")
    nuevoTelefono=input("Telefono: ")
    nuevoCorreo=input("Correo: ")
    nuevaPassword=input("Contraseña: ")
    nuevoRol="camper"
    nuevoestado="Proceso de Ingreso"
    nuevoriesgo="ninguno"

    base_path = os.path.dirname(__file__)
    ##Agregar informacion a camper
    ruta = os.path.join(os.path.dirname(__file__), "campers.json")

    if not os.path.exists(ruta):
        with open(ruta, "w") as archivo:
            json.dump([], archivo)

    with open(ruta, "r") as archivo:
        campers_data = json.load(archivo)

    # Support two possible file structures:
    # - a list (old/new simple format)
    # - a dict with key 'lista_Campers' (existing file in repo)
    if isinstance(campers_data, dict) and "lista_Campers" in campers_data and isinstance(campers_data["lista_Campers"], list):
        campers_list = campers_data["lista_Campers"]
        campers_wrap = "dict"
    elif isinstance(campers_data, list):
        campers_list = campers_data
        campers_wrap = "list"
    else:
        campers_list = []
        campers_wrap = "list"

    nuevo_camper={
        "identificacion":nuevoIdentificacion,
        "nombres":nuevoNombre,
        "apellidos":nuevoApellido,
        "direccion":nuevoDireccion,
        "acudiente":nuevoAcudiente,
        "telefono":nuevoTelefono,
        "correo":nuevoCorreo,
        "password":nuevaPassword,
        "estado":nuevoestado,
        "riesgo":nuevoriesgo
    }    

    campers_list.append(nuevo_camper)

    # Write back preserving the original structure when possible
    if campers_wrap == "dict":
        campers_data["lista_Campers"] = campers_list
        to_write = campers_data
    else:
        to_write = campers_list

    with open(ruta, "w") as archivo:
        json.dump(to_write, archivo, indent=4)

    ##Agregar la cuenta 
    ruta_cuentas = os.path.join(base_path, "cuentas.json")

    if not os.path.exists(ruta_cuentas):
        with open(ruta_cuentas, "w") as archivo:
            json.dump([], archivo)

    with open(ruta_cuentas, "r") as archivo:
        cuentas = json.load(archivo)  

    nueva_cuenta={
        "correo":nuevoCorreo,
        "password":nuevaPassword,
        "rol":nuevoRol
    }  

    cuentas.append(nueva_cuenta)
    with open(ruta_cuentas, "w") as archivo:
        json.dump(cuentas, archivo, indent=4)

    print("Camper registrado correctamente ✅")