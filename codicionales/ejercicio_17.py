
numero = int(input("Introduce el número obtenido al lanzar el dado (1-6): "))

caras = {
    1: "seis",
    2: "cinco",
    3: "cuatro",
    4: "tres",
    5: "dos",
    6: "uno"
}

if numero >= 1 and numero <= 6:
    print("La cara opuesta es:", caras[numero])
else:
    print("ERROR: número incorrecto.")