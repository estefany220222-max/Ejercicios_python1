if __name__ == "__main__":
    n_eq = 3  
    eq = []    
    resuls = [] 
    print(" Registro de Partidos ")
    for i in range(n_eq):
        eq_1 = input(f"\nIntroduce el nombre del equipo 1 del partido {i+1}: ")
        eq_2 = input(f"Introduce el nombre del equipo 2 del partido {i+1}: ")
        eq.append([eq1, eq2])
        gol_1 = int(input(f"Introduce los goles metidos por {eq_1}: "))
        gol_2 = int(input(f"Introduce los goles metidos por {eq_2}: "))
        resuls.append([gol_1, gol_2])
    print("\nQUINIELA")
    for i in range(n_eq):
        eq_loc = eq[i][0]
        eq_vis = eq[i][1]
        gol_loc = resuls[i][0]
        gol_vis = resuls[i][1]
        if gol_loc > gol_vis:
            print(f"{eq_loc} - {eq_vis} -> 1")
        elif gol_loc < gol_vis:
            print(f"{eq_loc} - {eq_vis} -> 2")
        else:
            print(f"{eq_loc} - {eq_vis} -> X") 
