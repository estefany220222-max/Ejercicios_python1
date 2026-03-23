

mes = int(input("Introduce el número de mes (1-12): "))
year = int(input("Introduce el año: "))

if mes in [1, 3, 5, 7, 8, 10, 12]:
    print("31 días")
elif mes == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("29 días")
    else:
        print("28 días")
elif mes in [4, 6, 9, 11]:
    print("30 días")
else:
    print("Mes incorrecto")