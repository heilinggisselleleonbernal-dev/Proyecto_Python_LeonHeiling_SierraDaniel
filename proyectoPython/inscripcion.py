import json
import os

def proceso_inscripcion():
    print("Bienvenido a Campusland")

    nuevoIdentificacion = input("Numero de identificacion: ")
    nuevoNombre = input("Nombres: ")
    nuevoApellido = input("Apellidos: ")
    nuevoDireccion = input("Direccion: ")
    nuevoAcudiente = input("Nombre del acudiente: ")
    nuevoTelefono = input("Telefono: ")
    nuevoCorreo = input("Correo: ")
    nuevaPassword = input("Contraseña: ")

    nuevoRol = "camper"
    nuevoestado = "Proceso de Ingreso"
    nuevoriesgo = "ninguno"
    grupo = None

    base_path = os.path.dirname(__file__)
    ruta = os.path.join(base_path, "campers.json")

    # ✅ Si no existe → crear estructura correcta
    if not os.path.exists(ruta):
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump({"lista_Campers": []}, archivo, indent=4)

    # ✅ Cargar SIEMPRE como diccionario
    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        campers_list = datos.get("lista_Campers", [])

    nuevo_camper = {
        "identificacion": nuevoIdentificacion,
        "nombres": nuevoNombre,
        "apellidos": nuevoApellido,
        "direccion": nuevoDireccion,
        "acudiente": nuevoAcudiente,
        "telefono": nuevoTelefono,
        "correo": nuevoCorreo,
        "password": nuevaPassword,
        "estado": nuevoestado,
        "riesgo": nuevoriesgo,
        "grupo": grupo
    }

    campers_list.append(nuevo_camper)

    # ✅ Guardar estructura CONSISTENTE
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump({"lista_Campers": campers_list}, archivo, indent=4, ensure_ascii=False)

    # ---------- CUENTAS ----------
    ruta_cuentas = os.path.join(base_path, "cuentas.json")

    if not os.path.exists(ruta_cuentas):
        with open(ruta_cuentas, "w", encoding="utf-8") as archivo:
            json.dump([], archivo, indent=4)

    with open(ruta_cuentas, "r", encoding="utf-8") as archivo:
        cuentas = json.load(archivo)

    nueva_cuenta = {
        "correo": nuevoCorreo,
        "password": nuevaPassword,
        "rol": nuevoRol
    }

    cuentas.append(nueva_cuenta)

    with open(ruta_cuentas, "w", encoding="utf-8") as archivo:
        json.dump(cuentas, archivo, indent=4, ensure_ascii=False)

    print("Camper registrado correctamente ✅")
