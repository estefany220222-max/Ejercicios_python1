

num_alumnos = int(input("¿Cuántos alumnos participan en la actividad?: "))

if num_alumnos >= 100:
    coste_por_alumno = 65
elif num_alumnos >= 50 and num_alumnos <= 99:
    coste_por_alumno = 70
elif num_alumnos >= 30 and num_alumnos <= 49:
    coste_por_alumno = 95
elif num_alumnos < 30 and num_alumnos > 0:
    coste_por_alumno = 4000 / num_alumnos
else:
    coste_por_alumno = 0

if num_alumnos > 0:
    coste_autobus = num_alumnos * coste_por_alumno
    print("El coste por alumno es", coste_por_alumno, "euros.")
    print("El coste del autobús es", coste_autobus, "euros.")
else:
    print("El número de alumnos debe ser un valor positivo.")