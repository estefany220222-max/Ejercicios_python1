hp = int(input("Hora de salida: "))
mp = int(input("Minutos de salida: "))
sp = int(input("Segundos de salida: "))
sv = int(input("Tiempo que tardaste en segundos: "))

si = hp * 3600 + mp * 60 + sp

hll = (si + sv) / 3600
mll = ((si + sv) % 3600 ) / 60
sll = ((si + sv) % 3600 ) % 60

print("Hora de llegada", hll, ".", mll, ".", sll)
