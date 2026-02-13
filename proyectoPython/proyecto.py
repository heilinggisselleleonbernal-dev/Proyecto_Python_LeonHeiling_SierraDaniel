import json
import os
from coordinador import menu_Coordinador
from inscripcion import proceso_inscripcion

def cargar_Usuarios():
    ruta = os.path.join(os.path.dirname(__file__), "cuentas.json")

    if not os.path.exists(ruta):
        with open(ruta, "w") as archivo:
            json.dump([], archivo)

    with open(ruta, "r") as archivo:
        return json.load(archivo)

while True:
    print("1. inicia sesion")
    print("2. registrarse")
    opcion = int(input("seleccione una opcion: "))
    if opcion == 1:
        usuarios =  cargar_Usuarios()
        correo= input ("ingrese su correo: ")
        password=input("ingrese su contraseña: ")
        encontrado= False
        for usuario in usuarios:
            if usuario["correo"] == correo and usuario["password"] == password:
                encontrado = True
                print("haz iniciado sesion")
                if usuario["rol"] == "coordinador":
                   menu_Coordinador()
                break
        
        if not encontrado:
            print("el usuario no fue encontrado")
    
    elif opcion == 2:
        proceso_inscripcion()

