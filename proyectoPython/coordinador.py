
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
                    print(f"No existe el archivo de campers: {ruta}")
                except json.JSONDecodeError:
                    print(f"El archivo {ruta} contiene JSON inválido")
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
                            if nuevo_estado in ["Proceso de Ingreso", "Inscrito", "Aprobado", "cursando", "Graduado", "Retirado","expulsado"]:
                                camper["estado"] = nuevo_estado
                                with open(ruta, "w", encoding="utf-8") as archivo:
                                    json.dump(datos, archivo, indent=4)
                                print("✅ Estado actualizado correctamente")
                            encontrado = True
                            break
                    if not encontrado:
                        print("❌ Camper no encontrado")
            if subopcion == 3:
                print("volviendo al menu principal")
                break
        elif opcion == 2:
            print("1.añadir trainers")
            print("2.editar trainers")
            print("3.listar trainers")
            print("4.eliminar trainers")
            print ("5.volver")
            subopcion_raw=input("seleccione una opcion: ")
            try:
                subopcion=int(subopcion_raw)
            except ValueError:
                print("Entrada inválida, ingrese un número.")
                continue
            
            if subopcion == 1:
                try:
                    ruta = os.path.join(os.path.dirname(__file__), "trainer.json")
                    nuevoNombre=input("Nombre: ")
                    nuevoApellido=input("Apellido: ")
                    nuevoCorreo=input("Correo: ")
                    nuevaPassword=input("Contraseña: ")
                    nuevasEspecialidades=input("Especialidades (separadas por comas): ").split(",")
                    nuevasEspecialidades = [e.strip() for e in nuevasEspecialidades]
                    nuevoRol="trainer"
                    base_path = os.path.dirname(__file__)

                    if not os.path.exists(ruta):
                        with open(ruta, "w") as archivo:
                            json.dump({"lista_Trainers": []}, archivo)

                    with open(ruta, "r") as archivo:
                        trainers_data = json.load(archivo)
                    if isinstance(trainers_data, dict) and "lista_Trainers" in trainers_data and isinstance(trainers_data["lista_Trainers"], list):
                        trainers_list = trainers_data["lista_Trainers"]
                        trainers_wrap = "dict"
                    elif isinstance(trainers_data, list):
                        trainers_list = trainers_data
                        trainers_wrap = "list"
                    else:
                        trainers_list = []
                        trainers_wrap = "dict"

                    nuevo_trainer={
                        "nombre":nuevoNombre,
                        "apellido":nuevoApellido,
                        "correo":nuevoCorreo,
                        "password":nuevaPassword,
                        "especialidad":nuevasEspecialidades
                    }    

                    trainers_list.append(nuevo_trainer)

                    if trainers_wrap == "dict":
                        trainers_data["lista_Trainers"] = trainers_list
                        to_write = trainers_data
                    else:
                        to_write = trainers_list

                    with open(ruta, "w") as archivo:
                        json.dump(to_write, archivo, indent=4)

                    
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
                    print("trainer fue añadido correctamente ✅")
                except FileNotFoundError:
                    print(f"No existe el archivo de trainers: {ruta}")
                except json.JSONDecodeError:
                    print(f"El archivo {ruta} contiene JSON inválido")
                        
            elif subopcion == 2:
                ruta = os.path.join(os.path.dirname(__file__), "trainer.json")
                try:
                    with open(ruta, "r", encoding="utf-8") as archivo:
                        datos = json.load(archivo)
                        trainers = datos.get("lista_Trainers", [])
                        correo_buscar = input("Ingrese correo del trainer: ")
                        encontrado = False
                        for trainer in trainers:
                            if trainer.get("correo") == correo_buscar:
                                print("✅ Trainer encontrado")
                                print("Nombre:", trainer.get("nombre"), trainer.get("apellido"))
                                print("Correo:", trainer.get("correo"))
                                print("Especialidad:", ", ".join(trainer.get("especialidad", [])))
                                print("¿Qué desea editar?")
                                print("1. Nombre")
                                print("2. Apellido")
                                print("3. Correo")
                                print("4. Especialidad")
                                campo = int(input("Seleccione: "))
                                
                                if campo == 1:
                                    trainer["nombre"] = input("Nuevo nombre: ")
                                elif campo == 2:
                                    trainer["apellido"] = input("Nuevo apellido: ")
                                elif campo == 3:
                                    trainer["correo"] = input("Nuevo correo: ")
                                elif campo == 4:
                                    nuevas_especialidades = input("Nuevas especialidades (separadas por coma): ").split(",")
                                    trainer["especialidad"] = [e.strip() for e in nuevas_especialidades]
                                
                                with open(ruta, "w", encoding="utf-8") as archivo:
                                    json.dump(datos, archivo, indent=4)
                                print("✅ Datos actualizados correctamente")
                                encontrado = True
                                break
                        if not encontrado:
                            print("❌ Trainer no encontrado")
                except FileNotFoundError:
                    print(f"No existe el archivo de trainers: {ruta}")
                except json.JSONDecodeError:
                    print(f"El archivo {ruta} contiene JSON inválido")
                    
            elif subopcion == 3:
                ruta = os.path.join(os.path.dirname(__file__), "trainer.json")
                try:
                    with open(ruta, "r", encoding="utf-8") as archivo:
                        datos = json.load(archivo)
                        trainers = datos.get("lista_Trainers", [])
                    if not trainers:
                        print("No hay trainers registrados")
                    else:
                        for trainer in trainers:
                            print("Nombre:", trainer.get("nombre"), trainer.get("apellido"))
                            print("Correo:", trainer.get("correo"))
                            print("Especialidad:", ", ".join(trainer.get("especialidad", [])))
                            print("---")
                except FileNotFoundError:
                    print(f"No existe el archivo de trainers: {ruta}")
                except json.JSONDecodeError:
                    print(f"El archivo {ruta} contiene JSON inválido")
                    
            elif subopcion == 4:
                ruta = os.path.join(os.path.dirname(__file__), "trainer.json")
                try:
                    with open(ruta, "r", encoding="utf-8") as archivo:
                        datos = json.load(archivo)
                        trainers = datos.get("lista_Trainers", [])
                        id_buscar = input("Ingrese identificación del trainer a eliminar: ")
                        encontrado = False
                        for i, trainer in enumerate(trainers):
                            if trainer.get("correo") == correo_buscar:
                                print("✅ Trainer encontrado")
                                print("Nombre:", trainer.get("nombre"), trainer.get("apellido"))
                                confirmacion = input("¿Está seguro de que desea eliminar este trainer? (si/no): ")
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
                    print(f"No existe el archivo de trainers: {ruta}")
                except json.JSONDecodeError:
                    print(f"El archivo {ruta} contiene JSON inválido")
                    
            elif subopcion == 5:
                print("Volviendo al menú principal...")
                break
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
                        if nota >= 40:
                            print("✅ Camper APROBADO")
                            camper["estado"] = "Aprobado"
                            break
                        else:
                            print("❌ Nota insuficiente → Debe repetir la prueba")
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
            ruta = os.path.join(os.path.dirname(__file__), "campers.json")
            try:
                with open(ruta, "r", encoding="utf-8") as archivo:
                    datos = json.load(archivo)
                campers = datos.get("lista_Campers", [])
                if not campers:
                    print("No hay campers registrados")
                    return
                id_buscar = input("Ingrese ID del camper: ")
                grupo_nuevo = input("Ingrese grupo a asignar: ")
                encontrado = False
                for camper in campers:
                    if camper["identificacion"] == id_buscar:
                        camper["grupo"] = grupo_nuevo
                        encontrado = True
                        break
                if not encontrado:
                    print("Camper no encontrado ❌")
                    return
                with open(ruta, "w", encoding="utf-8") as archivo:
                    json.dump(datos, archivo, indent=4)
                print("Grupo asignado correctamente ✅")
            except FileNotFoundError:
                print("No existe campers.json ❌")
            except json.JSONDecodeError:
                print("JSON dañado ❌")
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
            except json.JSONDecodeError:
                print("JSON dañado ❌")
        elif opcion == 7:
            ruta = os.path.join(os.path.dirname(__file__), "grupos.json")
            try:
                with open(ruta, "r", encoding="utf-8") as archivo:
                    grupos = json.load(archivo)
                if not grupos:
                    print("No hay grupos registrados")
                    return
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
                    return
                with open(ruta, "w", encoding="utf-8") as archivo:
                    json.dump(grupos, archivo, indent=4)
                print("Ruta asignada correctamente ✅")
            except FileNotFoundError:
                print("No existe grupos.json ❌")
            except json.JSONDecodeError:
                print("JSON dañado ❌")
        elif opcion == 8:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

    
                
                
