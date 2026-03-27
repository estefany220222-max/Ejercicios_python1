car = input('Escribe una letra (" " para salir): ')
while car != " ":
    if len(car) == 1:  # Aseguramos que sea solo un carácter
        if car.upper() in ['A', 'E', 'I', 'O', 'U']:
            print("Vocal")
        else:
            print("No vocal")
    else:
        print("Por favor escribe solo un carácter.")

    car = input('Escribe una letra (" " para salir): ')
