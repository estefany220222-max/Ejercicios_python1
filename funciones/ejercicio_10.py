def c_seg(h, m, s):
    seg = h * 3600 + m * 60 + s
    return seg

def c_hms(seg):
    h = int(seg/3600)
    seg = seg-h*3600
    m = int(seg/60)
    seg = seg-m*60
    s = seg
    return h, m, s
opcion = 0
while opcion != 3:
    print("1.- Convertir a segundos")
    print("2.- Convertir a horas, minutos y segundos")
    print("3.- Salir")
    opcion = int(input( "Elige una opción: "))
    if opcion == 1:
        hor = int(input("Horas: "))
        minu = int(input("Minutos: "))
        seg = int(input("Segundos: "))
        print("Corresponde a", convertir_a_segundos(hor, minu, seg), "segundos.")
    elif opcion == 2:
        segund = int(input("Segundos: "))
        resultado = convertir_a_hms(segund)
        hor = resultado[0]
        minu = resultado[1]
        seg = resultado[2]
        print("Corresponde a", hor, ":", minu, ":", seg)
    elif opcion == 3:
        pass
    else:
        print("Opción incorrecta")
