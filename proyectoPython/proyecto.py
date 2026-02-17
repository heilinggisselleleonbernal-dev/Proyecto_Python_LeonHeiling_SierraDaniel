import json
import os
from coordinador import menu_Coordinador
from inscripcion import proceso_inscripcion
from menuCamper import menuCamper
from menuTrainer import menuTrainer
from crear_Grupos import crear_grupos

def cargar_Usuarios():
    ruta = os.path.join(os.path.dirname(__file__), "cuentas.json")

    if not os.path.exists(ruta):
        with open(ruta, "w") as archivo:
            json.dump([], archivo)

    with open(ruta, "r") as archivo:
        return json.load(archivo)

while True:
    print("------------Bienvenido a Campusland------------")
    print("1. 🔑 inicia sesion")
    print("2. 📝 registrarse")
    opcion = int(input(" seleccione una opcion: "))
    if opcion == 1:
        usuarios =  cargar_Usuarios()
        correo= input ("➡ingrese su correo: ")
        password=input("➡ingrese su contraseña: ")
        encontrado= False
        for usuario in usuarios:
            if usuario["correo"] == correo and usuario["password"] == password:
                encontrado = True
                print("✔ has iniciado sesion")
                if usuario["rol"] == "coordinador":
                    print("👋bienvenido coordinador")
                    menu_Coordinador()
                    break
                elif usuario["rol"] == "trainer":
                    print("👋bienvenido trainer")
                    try:
                        with open(os.path.join(os.path.dirname(__file__), "trainer.json"), "r", encoding="utf-8") as archivo:
                            trainers_data = json.load(archivo)
                            trainers_list = trainers_data.get("lista_Trainers", [])
                            for t in trainers_list:
                                if t.get("correo") == usuario.get("correo"):
                                    usuario["id"] = t.get("id")
                                    break
                    except Exception:
                        pass
                    menuTrainer(usuario)
                    break
                elif usuario["rol"] == "camper":
                    print("👋bienvenido camper")
                    menuCamper()
                    break
        
        if not encontrado:
            print("❌el usuario no fue encontrado")
    
    elif opcion == 2:
        proceso_inscripcion()


