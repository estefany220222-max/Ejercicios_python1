def caper(r):
    pi = 3.1416
    a = pi * r ** 2
    per = 2 * pi * r
    return a, per
r = float(input("Introduce el radio: "))
resul = caper(r)
a = resul[0]
per = resul[1]
print("Área:", a)
print("Perímetro:", per)



