while True:
    print("\nMenú de recomendaciones\n1.Literatura\n2.Cine\n3.Música\n4.Videojuegos\n5. Salir\n")
    opc = int(input("Elija una opción: "))
    if opc == 1:
        print("Lecturas recomendables:")
        print(" + Esperándolo a Tito y otros cuentos de fútbol (Eduardo Sacheri)")
        print(" + El juego de Ender (Orson Scott Card)")
        print(" + El sueño de los héroes (Adolfo Bioy Casares)")
    elif opc == 2:
        print("Películas recomendables:")
        print(" + Matrix (1999)")
        print(" + El último samuray (2003)")
        print(" + Cars (2006)")
    elif opc == 3:
        print("Discos recomendables:")
        print(" + Despedazado por mil partes (La Renga, 1996)")
        print(" + Búfalo (La Mississippi, 2008)")
        print(" + Gaia (Mägo de Oz, 2003)")
    elif opc == 4:
        print("Videojuegos clásicos recomendables:")
        print(" + Día del tentáculo (LucasArts, 1993)")
        print(" + Terminal Velocity (Terminal Reality/3D Realms, 1995)")
        print(" + Death Rally (Remedy/Apogee, 1996)")
    elif opc == 5:
        print("Gracias, vuelva pronto")
        break
    else:
        print("Opción no válida")
    input("Presione enter para continuar...")
