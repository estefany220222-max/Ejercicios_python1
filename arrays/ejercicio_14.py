if __name__ == "__main__":
    precs = []
    cant = []
    print(" Sistema de Inventario y Ventas ")
    print("\nRegistro de Precios:")
    for i in range(5):
        prec = float(input(f"Ingrese Precio del Articulo {i+1}: $"))
        precs.append(prec)
    print("\nRegistro de Cantidades por Sucursal:")
    for suc in range(4):
        print(f" Sucursal {suc+1} ")
        c_art = []
        for art in range(5):
            cant = float(input(f"Ingrese Cantidad de Articulo {art+1}: "))
            c_art.append(cant)
        cant.append(c_art)
    print("\n--- Reporte de Inventario ---")
    print("Cantidades totales por artículos en todas las sedes:")
    for art in range(5):
        s_art = cant[0][art] + cant[1][art] + cant[2][art] + cant[3][art]
        print(f"Total articulo {art+1}: {s_art} unidades")
    art_suc2 = sum(cant[1])
    print(f"\nTotal de artículos en la Sucursal 2: {art_suc2}")
    print(f"Cantidad exacta en Sucursal 1, Articulo 3: {cant[0][2]}")
    may_rec = 0
    n_mayor = 0
    totalem = 0
    print("\n Reporte Financiero ")
    for suc in range(4):
        t_suc = 0
        for art in range(5):
            t_suc = t_suc + (cant[suc][art] * precs[art])
        print(f"Recaudación Sucursal {suc+1}: ${t_suc}")
        if t_suc > may_rec:
            may_rec = t_suc
            num_mayor = suc + 1
        totalem = totalem + t_suc
        
    print(f"Recaudación total de la empresa: ${totalem}")
    print(f"Sucursal de Mayor Recaudación: Sucursal {n_mayor}")
