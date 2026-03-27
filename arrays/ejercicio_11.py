if __name__ == "__main__":
    n_filas = 5
    n_cols = 5
    matriz = []  
    for fila in range(n_filas):
        fila_act = []
        for col in range(n_cols):
            if fila == col or fila == (n_filas - 1) - col:
                fila_act.append(1)
            else:
                fila_act.append(0)
        matriz.append(fila_act)
    print(" Matriz con Diagonales en X ")
    for fila in range(n_filas):
        for col in range(n_cols):
            print(matriz[fila][col], end=" ")
        print()
        
