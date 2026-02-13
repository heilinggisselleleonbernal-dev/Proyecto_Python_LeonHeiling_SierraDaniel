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
        campers = json.load(archivo)

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

    campers.append(nuevo_camper)
    with open(ruta, "w") as archivo:
        json.dump(campers, archivo, indent=4)

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