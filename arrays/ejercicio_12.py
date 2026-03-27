if __name__ == "__main__":
    n_filas = 5
    n_cols = 15
    matriz = []  
    for fila in range(n_filas):
        fila_act = []
        for col in range(n_cols):
            if fila == 0 or fila == n_filas - 1 or col == 0 or col == n_cols - 1:
                fila_act.append(1) 
            else:
                fila_act.append(0) 
        matriz.append(fila_act)
    print(" Perímetro de Seguridad ")
    for fila in range(n_filas):
        for col in range(n_cols):
            print(matriz[fila][col], end=" ") 
        print()
