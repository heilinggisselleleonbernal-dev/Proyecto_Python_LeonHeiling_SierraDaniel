import json
import os
from crear_Grupos import crear_grupos

def menu_Coordinador():
    while True:
        print("1.gestiona campers")
        print("2.gestiona trainers")
        print("3.aprobar prueba de ingreso")
        print("4.crear grupos")
        print("5.asignar camper a grupo")
        print("6.listar campers por estado")
        print("7.asignar ruta al grupo")
        print("8.salir")

        opcion_raw = input("seleccione:")
        try:
            opcion = int(opcion_raw)
        except ValueError:
            print("Entrada inválida, ingrese un número.")
            continue

        if opcion == 1:
            print("----CAMPERS-----")
            print("1.listar campers")
            print("2.editar campers")
            print("3.volver")

            subopcion_raw = input("seleccione: ")
            try:
                subopcion = int(subopcion_raw)
            except ValueError:
                print("Entrada inválida, ingrese un número.")
                continue

            if subopcion == 1:
                try:
                    ruta = os.path.join(os.path.dirname(__file__), "campers.json")
                    with open(ruta, "r", encoding="utf-8") as archivo:
                        datos = json.load(archivo)
                        campers = datos.get("lista_Campers", [])

                    if not campers:
                        print("No hay campers registrados")
                    else:
                        for camper in campers:
                            print("ID:", camper["identificacion"])
                            print("Nombre:", camper["nombres"], camper["apellidos"])
                            print("Estado:", camper["estado"])

                except FileNotFoundError:
                    print(f"No existe el archivo de campers")

            if subopcion == 2:
                ruta = os.path.join(os.path.dirname(__file__), "campers.json")

                with open(ruta, "r", encoding="utf-8") as archivo:
                    datos = json.load(archivo)
                    campers = datos.get("lista_Campers", [])

                id_buscar = input("Ingrese identificación: ")
                encontrado = False

                for camper in campers:
                    if camper["identificacion"] == id_buscar:
                        print("✅ Camper encontrado")
                        print("ID:", camper["identificacion"])
                        print("Nombre:", camper["nombres"], camper["apellidos"])
                        print("Estado:", camper["estado"])

                        nuevo_estado = input("Ingrese nuevo estado: ")

                        if nuevo_estado in [
                            "Proceso de Ingreso",
                            "Inscrito",
                            "Aprobado",
                            "Cursando",
                            "Graduado",
                            "Retirado",
                            "Expulsado"
                        ]:
                            camper["estado"] = nuevo_estado

                            with open(ruta, "w", encoding="utf-8") as archivo:
                                json.dump({"lista_Campers": campers}, archivo, indent=4)

                            print("✅ Estado actualizado correctamente")
                        else:
                            print("❌ Estado inválido")

                        encontrado = True
                        break

                if not encontrado:
                    print("❌ Camper no encontrado")

            if subopcion == 3:
                print("volviendo al menu principal")
                continue 

        elif opcion == 2:
            print("1.añadir trainers")
            print("2.editar trainers")
            print("3.listar trainers")
            print("4.eliminar trainers")
            print("5.volver")

            subopcion_raw = input("seleccione una opcion: ")
            try:
                subopcion = int(subopcion_raw)
            except ValueError:
                print("Entrada inválida, ingrese un número.")
                continue

            ruta = os.path.join(os.path.dirname(__file__), "trainer.json")

            if subopcion == 1:
                try:
                    nuevoNombre = input("Nombre: ")
                    nuevoApellido = input("Apellido: ")
                    nuevoCorreo = input("Correo: ")
                    nuevaPassword = input("Contraseña: ")
                    nuevasEspecialidades = input("Especialidades (separadas por comas): ").split(",")
                    nuevasEspecialidades = [e.strip() for e in nuevasEspecialidades]

                    if not os.path.exists(ruta):
                        with open(ruta, "w") as archivo:
                            json.dump({"lista_Trainers": []}, archivo)

                    with open(ruta, "r") as archivo:
                        datos = json.load(archivo)

                    datos["lista_Trainers"].append({
                        "nombre": nuevoNombre,
                        "apellido": nuevoApellido,
                        "correo": nuevoCorreo,
                        "password": nuevaPassword,
                        "especialidad": nuevasEspecialidades
                    })

                    with open(ruta, "w") as archivo:
                        json.dump(datos, archivo, indent=4)

                    print("trainer fue añadido correctamente ✅")

                except FileNotFoundError:
                    print("No existe trainer.json")

            elif subopcion == 4:
                try:
                    with open(ruta, "r", encoding="utf-8") as archivo:
                        datos = json.load(archivo)

                    trainers = datos.get("lista_Trainers", [])

                    correo_buscar = input("Ingrese correo del trainer a eliminar: ")
                    encontrado = False

                    for i, trainer in enumerate(trainers):
                        if trainer.get("correo") == correo_buscar:
                            print("✅ Trainer encontrado")
                            print("Nombre:", trainer.get("nombre"), trainer.get("apellido"))

                            confirmacion = input("¿Está seguro? (si/no): ")
                            if confirmacion.lower() == "si":
                                trainers.pop(i)

                                with open(ruta, "w", encoding="utf-8") as archivo:
                                    json.dump(datos, archivo, indent=4)

                                print("✅ Trainer eliminado correctamente")
                            else:
                                print("Operación cancelada")

                            encontrado = True
                            break

                    if not encontrado:
                        print("❌ Trainer no encontrado")

                except FileNotFoundError:
                    print("No existe trainer.json")

            elif subopcion == 5:
                continue

        elif opcion == 3:
            ruta = os.path.join(os.path.dirname(__file__), "campers.json")

            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            campers = datos.get("lista_Campers", [])
            id_buscar = input("Ingrese identificación del camper: ")

            encontrado = False

            for camper in campers:
                if camper["identificacion"] == id_buscar:
                    while True:
                        try:
                            nota = float(input("Ingrese la nota de la prueba inicial: "))

                            if nota < 0 or nota > 100:
                                print("❌ Nota inválida (0 - 100)")
                                continue

                        except ValueError:
                            print("❌ Debe ingresar un número válido")
                            continue

                        if nota >= 60:
                            print("✅ Camper APROBADO")
                            camper["estado"] = "Aprobado"
                        else:
                            print("❌ Nota insuficiente")
                            camper["estado"] = "Proceso de Ingreso"

                        break

                    encontrado = True
                    break

            if encontrado:
                with open(ruta, "w", encoding="utf-8") as archivo:
                    json.dump(datos, archivo, indent=4)
            else:
                print("❌ Camper no encontrado")

        elif opcion == 4:
            crear_grupos()

        elif opcion == 5:
            ruta_campers = os.path.join(os.path.dirname(__file__), "campers.json")
            ruta_grupos = os.path.join(os.path.dirname(__file__), "grupos.json")

            try:
                with open(ruta_campers, "r", encoding="utf-8") as archivo:
                    datos = json.load(archivo)

                campers = datos.get("lista_Campers", [])

                if not campers:
                    print("No hay campers registrados")
                    continue 

                id_buscar = input("Ingrese ID del camper: ")
                grupo_nuevo = input("Ingrese grupo a asignar: ")

                encontrado = False
                camper_info = None

                for camper in campers:
                    if camper["identificacion"] == id_buscar:
                        camper["grupo"] = grupo_nuevo
                        camper_info = camper
                        encontrado = True
                        break

                if not encontrado:
                    print("Camper no encontrado ❌")
                    continue

                with open(ruta_campers, "w", encoding="utf-8") as archivo:
                    json.dump(datos, archivo, indent=4)

                with open(ruta_grupos, "r", encoding="utf-8") as archivo:
                    grupos = json.load(archivo)

                grupo_encontrado = False

                for grupo in grupos:
                    if grupo.get("idGrupo") == grupo_nuevo:

                        ya_esta = any(c["identificacion"] == id_buscar for c in grupo.get("campers", []))

                        if not ya_esta:
                            grupo.setdefault("campers", []).append({
                                "identificacion": camper_info["identificacion"],
                                "nombre": camper_info.get("nombres", ""),
                                "apellidos": camper_info.get("apellidos", "")
                            })

                        grupo_encontrado = True
                        break

                if grupo_encontrado:
                    with open(ruta_grupos, "w", encoding="utf-8") as archivo:
                        json.dump(grupos, archivo, indent=4)

                    print("Grupo asignado correctamente ✅")
                else:
                    print("Grupo no encontrado ❌")

            except FileNotFoundError:
                print("No existe campers.json o grupos.json ❌")

        elif opcion == 6:
            ruta = os.path.join(os.path.dirname(__file__), "campers.json")

            try:
                with open(ruta, "r", encoding="utf-8") as archivo:
                    datos = json.load(archivo)

                campers = datos.get("lista_Campers", [])

                if not campers:
                    print("No hay campers registrados")
                else:
                    estado = input("Ingrese el estado a filtrar: ")

                    encontrados = [c for c in campers if c.get("estado") == estado]

                    if not encontrados:
                        print(f"No hay campers con estado '{estado}'")
                    else:
                        for camper in encontrados:
                            print("ID:", camper["identificacion"])
                            print("Nombre:", camper["nombres"], camper["apellidos"])
                            print("Estado:", camper["estado"])
                            print("---")

            except FileNotFoundError:
                print("No existe campers.json ❌")

        elif opcion == 7:
            ruta = os.path.join(os.path.dirname(__file__), "grupos.json")

            try:
                with open(ruta, "r", encoding="utf-8") as archivo:
                    grupos = json.load(archivo)

                if not grupos:
                    print("No hay grupos registrados")
                    continue   

                id_grupo = input("Ingrese ID del grupo: ")
                nueva_ruta = input("Ingrese nueva ruta: ")

                encontrado = False

                for grupo in grupos:
                    if grupo.get("idGrupo") == id_grupo:
                        grupo["ruta"] = nueva_ruta
                        encontrado = True
                        break

                if not encontrado:
                    print("Grupo no encontrado ❌")
                    continue

                with open(ruta, "w", encoding="utf-8") as archivo:
                    json.dump(grupos, archivo, indent=4)

                print("Ruta asignada correctamente ✅")

            except FileNotFoundError:
                print("No existe grupos.json ❌")

        elif opcion == 8:
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, intente nuevamente.")

