vehiculo1 = input("Coloca la velocidad del coche 1: ")
vehiculo2 = input("Coloca la velocidad del coche 2: ")

dist = int(input("A que distancia se encuentran los coches? "))

time = dist / (vehiculo1 - vehiculo2)
time * 60

print("Lo alcanza en", time, "minutos")