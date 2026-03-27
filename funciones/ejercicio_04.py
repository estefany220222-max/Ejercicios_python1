def conv(cad):
    espacios = ""
    for let in cad:
        espacios += let + " "
    return espacios
if __name__ == "__main__":
    mens = input("Introduce una cadena: ")
    print("La cadena con espacio:")
    print(conv(mensaje))
