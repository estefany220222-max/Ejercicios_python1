

tiempo = int(input("¿Cuánto tiempo es la llamada?: "))
es_domingo = input("¿Es Domingo? (S/N): ").upper()
turno = ""

if es_domingo == "N":
    turno = input("¿Qué turno: Mañana o Tarde? (M/T)?: ").upper()

if tiempo < 5:
    coste = tiempo * 100
elif tiempo < 8:
    coste = (tiempo - 5) * 80 + 500
elif tiempo < 10:
    coste = (tiempo - 8) * 70 + 240 + 500
else:
    coste = (tiempo - 10) * 50 + 140 + 240 + 500

if es_domingo == "S":
    coste = coste + coste * 0.03
else:
    if turno == "M":
        coste = coste + coste * 0.15
    else:
        coste = coste + coste * 0.10

print("El coste de la llamada:", coste / 100, "euros.")