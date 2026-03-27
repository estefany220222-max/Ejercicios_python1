c_ds = 5
temp = [[0, 0] for _ in range(c_ds)]
for i in range(c_ds):
    temp[i][0] = float(input(f"Día {i+1}. Temperatura mínima: "))
    temp[i][1] = float(input(f"Día {i+1}. Temperatura máxima: "))
print("Temperaturas medias
for i in range(c_ds):
    print(f"Día {i+1}. Temperatura media: {(temp[i][0] + temp[i][1]) / 2}")
temp_min = temp[0][0]
for i in range(c_ds):
    if temp[i][0] < temp_min:
        temp_min = temp[i][0]
print("Días con menos temperatura")
for i in range(c_ds):
    if temp[i][0] == temp_min:
        print(f"Día {i+1}")
print("Días con temperatura máxima")
temp_max = float(input("Introduce una temperatura: "))
e_temp = False
for i in range(c_ds):
    if temp[i][1] == temp_max:
        print(f"Día {i+1}")
        e_temp = True
if not e_temp:
    print("No hay ningún día con dicha temperatura.")
