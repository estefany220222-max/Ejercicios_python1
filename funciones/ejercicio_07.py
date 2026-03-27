def login(nom, pas, ints):
    if nom == "usuario" and pas == "123456":
        log = True
    else:
        login = False
        ints = ints + 1
    return log, ints
c_veces = 0
ent = False
while ent == False and c_veces < 3:
    usuario = input("Usuario: ")
    clave = input("Password: ")
    resul = log(usuario, clave, cuantasveces)
    ent = resul[0]
    c_veces = resul[1]
    if ent == False:
        print("Error. Nombre de usuario o contraseña incorrecta.")
if ent == True:
    print("Bienvenidos al sistema")
else:
    print("No has entrado en el sistema")
