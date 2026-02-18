import json
import os

def cargar_grupos():
    ruta = os.path.join(os.path.dirname(__file__), "Grupos.json")
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def cargar_campers():
    ruta = os.path.join(os.path.dirname(__file__), "campers.json")
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        return datos.get("lista_Campers", [])

def menuCamper(correo):

    campers = cargar_campers()
    camper_logueado = next((c for c in campers if c["correo"] == correo), None)

    if not camper_logueado:
        print("❌ Camper no encontrado.")
        return

    id_camper = camper_logueado["identificacion"]

    while True:
        print("------ MENÚ CAMPER ------")
        print("1. 📄 Ver datos personales")
        print("2. 👥 Ver grupo asignado")
        print("3. 📊 Ver notas por módulo")
        print("4. ⚠ Revisar estado y riesgo")
        print("5. 🔚 Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if opcion == 1:
            print("------ 📄 DATOS PERSONALES ------")
            print("Identificación:", camper_logueado.get("identificacion"))
            print("Nombres:", camper_logueado.get("nombres"))
            print("Apellidos:", camper_logueado.get("apellidos"))
            print("Dirección:", camper_logueado.get("direccion"))
            print("Acudiente:", camper_logueado.get("acudiente"))
            print("Teléfono:", camper_logueado.get("telefono"))
            print("Correo:", camper_logueado.get("correo"))
            print("Estado:", camper_logueado.get("estado"))
            print("Riesgo:", camper_logueado.get("riesgo"))
            print("Grupo:", camper_logueado.get("grupo"))

        elif opcion == 2:
            grupos = cargar_grupos()
            encontrado = False

            for grupo in grupos:
                for camper in grupo["campers"]:
                    if camper["identificacion"] == id_camper:
                        print("------ 👥 TU GRUPO ------")
                        print("Grupo:", grupo["idGrupo"])
                        print("Ruta:", grupo["ruta"])
                        print("Salón:", grupo["salon"])
                        print("Horario:", grupo["horaInicio"], "-", grupo["horaFin"])
                        print("\nCampers en el grupo:")

                        for i in grupo["campers"]:
                            print("-", i.get("nombre"))

                        encontrado = True
                        break

            if not encontrado:
                print("No tienes grupo asignado.")

        elif opcion == 3:
            grupos = cargar_grupos()
            encontrado = False

            for grupo in grupos:
                for modulo in grupo["modulos"]:
                    for evaluacion in modulo["evaluaciones"]:
                        if evaluacion.get("idCamper") == id_camper:
                            print("📘 Módulo:", modulo["nombre"])
                            print("Actividad:", evaluacion.get("actividad"))
                            print("Práctica:", evaluacion.get("practica"))
                            print("Teórica:", evaluacion.get("teorica"))
                            print("Definitiva:", evaluacion.get("definitiva"))
                            print("Aprobado:", evaluacion.get("aprobado"))
                            print("-----------------------------")
                            encontrado = True

            if not encontrado:
                print("No tienes notas registradas todavía.")

        elif opcion == 4:
            print("------ ⚠ ESTADO ACADÉMICO ------")
            print("Estado:", camper_logueado.get("estado"))
            print("Nivel de riesgo:", camper_logueado.get("riesgo"))

        elif opcion == 5:
            print("Saliendo del menú camper...")
            break

        else:
            print("Opción no válida.")
