if __name__ == "__main__":
    tamc_max = 10
    ds = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    names = []    
    m_kms = [] 
    print(" Sistema de Flotilla ")
    while True:
        n_cond = int(input("¿Cuántos conductores tiene la empresa?: "))
        if n_cond <= tamc_max:
            break 
        else:
            print(f"Como máximo puedo guardar la información de {tamc_max} conductores.\n")
    for i in range(n_cond):
        name = input(f"\nNombre del conductor {i+1}: ")
        names.append(name)
        k_sem = [] 
        for dia in dias:
            km = int(input(f"¿Cuántos km ha realizado el {dia}?: "))
            k_sem.append(km)
        k_sem.append(0) 
        m_kms.append(k_sem)
    for i in range(n_cond):
        suma_kms = 0
        for j in range(7):
            suma_kms = suma_kms + m_kms[i][j]
        m_kms[i][7] = suma_kms
    print("\n Reporte Final ")
    for i in range(n_cond):
        print(f"{names[i]} ha realizado {m_kms[i][7]} kms en total.")
