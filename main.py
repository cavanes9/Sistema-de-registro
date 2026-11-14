def mostrar_menu():
    print("\n--- Sistema de registro y analisis de estudiantes ---")
    print("1. Registrar un estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Consultar el promedio de un estudiante")
    print("4. Mostrar estadisticas generales del grupo")
    print("5. Salir")
    print("6. Eliminar un estudiante")


def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)


def solicitar_calificacion(numero):
    while True:
        try:
            calificacion = float(input(f"Calificacion {numero} (0-100): "))
        except ValueError:
            print("Ingresa un numero valido.")
            continue

        if 0 <= calificacion <= 100:
            return calificacion

        print("La calificacion debe estar entre 0 y 100.")


def registrar_estudiante(estudiantes):
    identificacion = input("Numero de identificacion: ").strip()
    while not identificacion:
        print("La identificacion no puede estar vacia.")
        identificacion = input("Numero de identificacion: ").strip()

    for estudiante in estudiantes:
        if estudiante["identificacion"] == identificacion:
            print("Ya existe un estudiante con esa identificacion.")
            return

    nombre = input("Nombre: ").strip()
    while not nombre:
        print("El nombre no puede estar vacio.")
        nombre = input("Nombre: ").strip()

    calificaciones = tuple(
        solicitar_calificacion(numero) for numero in range(1, 4)
    )
    promedio = calcular_promedio(calificaciones)
    aprobado = promedio >= 70

    estudiantes.append(
        {
            "identificacion": identificacion,
            "nombre": nombre,
            "calificaciones": calificaciones,
            "promedio": promedio,
            "aprobado": aprobado,
            "situacion": "Aprobado" if aprobado else "Reprobado",
        }
    )
    print(f"Estudiante {nombre} registrado correctamente.")


def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("Todavia no hay estudiantes registrados.")
        return

    for estudiante in estudiantes:
        calificaciones = ", ".join(
            f"{calificacion:g}" for calificacion in estudiante["calificaciones"]
        )
        print(
            f"\nIdentificacion: {estudiante['identificacion']}"
            f"\nNombre: {estudiante['nombre']}"
            f"\nCalificaciones: {calificaciones}"
            f"\nPromedio: {estudiante['promedio']:.2f}"
            f"\nSituacion: {estudiante['situacion']}"
        )


def consultar_estudiante(estudiantes):
    identificacion = input("Identificacion del estudiante: ").strip()

    for estudiante in estudiantes:
        if estudiante["identificacion"] == identificacion:
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Promedio: {estudiante['promedio']:.2f}")
            print(f"Situacion: {estudiante['situacion']}")
            return

    print("No se encontro un estudiante con esa identificacion.")


def mostrar_estadisticas(estudiantes):
    if not estudiantes:
        print("Todavia no hay estudiantes registrados para mostrar estadisticas.")
        return

    cantidad_aprobados = 0
    cantidad_reprobados = 0
    suma_promedios = 0
    promedio_mas_alto = estudiantes[0]["promedio"]

    for estudiante in estudiantes:
        suma_promedios += estudiante["promedio"]
        if estudiante["aprobado"]:
            cantidad_aprobados += 1
        else:
            cantidad_reprobados += 1

        if estudiante["promedio"] > promedio_mas_alto:
            promedio_mas_alto = estudiante["promedio"]

    promedio_general = suma_promedios / len(estudiantes)
    print(f"Estudiantes registrados: {len(estudiantes)}")
    print(f"Promedio general del grupo: {promedio_general:.2f}")
    print(f"Aprobados: {cantidad_aprobados}")
    print(f"Reprobados: {cantidad_reprobados}")
    print(f"Promedio mas alto: {promedio_mas_alto:.2f}")


def eliminar_estudiante(estudiantes):
    identificacion = input("Identificacion del estudiante que deseas eliminar: ").strip()

    for indice, estudiante in enumerate(estudiantes):
        if estudiante["identificacion"] == identificacion:
            estudiantes.pop(indice)
            print(f"Se elimino a {estudiante['nombre']}.")
            return

    print("No se encontro un estudiante con esa identificacion.")


def main():
    estudiantes = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            registrar_estudiante(estudiantes)
        elif opcion == "2":
            mostrar_estudiantes(estudiantes)
        elif opcion == "3":
            consultar_estudiante(estudiantes)
        elif opcion == "4":
            mostrar_estadisticas(estudiantes)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        elif opcion == "6":
            eliminar_estudiante(estudiantes)
        else:
            print("Opcion no valida. Elige un numero del 1 al 6.")


if __name__ == "__main__":
    main()