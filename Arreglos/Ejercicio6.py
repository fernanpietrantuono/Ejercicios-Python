def mostrar_matriz(cuadrado):
    for fila_f1 in cuadrado:
        for elemento in fila_f1:
            print(elemento, end="\t")
        print()


def check_magico(cuadrado, n_d):
    if check_filas(cuadrado, n_d):
        if check_columnas(cuadrado, n_d):
            return check_diagonales(cuadrado)
        else:
            return False
    else:
        return False


def check_filas(cuadrado, n_d):
    suma1 = 0
    suma2 = 0
    suma3 = 0
    for i_f3 in range(n_d):
        print("Fila:", i_f3)
        for j_f3 in range(n_d):
            print(f"[{cuadrado[i_f3][j_f3]}]", end="")
            if i_f3 == 0:
                suma1 += cuadrado[i_f3][j_f3]
            if i_f3 == 1:
                suma2 += cuadrado[i_f3][j_f3]
            comp = suma1 == suma2
            if i_f3 == 2 and comp is True:
                suma3 += cuadrado[i_f3][j_f3]
        print("")
        print("")
    print("")
    filas = suma2 == suma3
    return filas


def check_columnas(cuadrado, n_d):
    suma1 = 0
    suma2 = 0
    suma3 = 0
    for j_f4 in range(n_d):
        print("Columna:", j_f4)
        for i_f4 in range(n_d):
            print(f"[{cuadrado[j_f4][i_f4]}]")
            if j_f4 == 0:
                suma1 += cuadrado[j_f4][i_f4]
            if j_f4 == 1:
                suma2 += cuadrado[j_f4][i_f4]
            comp = suma1 == suma2
            if j_f4 == 2 and comp is True:
                suma3 += cuadrado[j_f4][i_f4]
        print("")
        print("")
    columnas = suma2 == suma3
    return columnas


def check_diagonales(cuadrado):
    suma1 = 0
    suma2 = 0
    for i_f5 in range(len(cuadrado)):
        suma1 += cuadrado[i_f5][i_f5]
    j_f5 = len(cuadrado) - 1
    for i_f5 in range(len(cuadrado)):
        suma2 += cuadrado[i_f5][j_f5]
        j_f5 -= 1
    diagonales = suma1 == suma2
    return diagonales


n = int(input("Dimensioná el tamaño del cuadrado: "))
matriz = []
for i in range(n):
    fila = []
    print(f"Fila {i}:")
    for j in range(n):
        num = int(input(f"Ingresá un valor para la posición {i},{j}: "))
        while num < 1 or num > 9:
            num = int(input("El valor ingresado no está dentro de los parámetros, por favor, inténtelo nuevamente: "))
        fila.append(num)
    matriz.append(fila)
print("\nCuadrado: ")
mostrar_matriz(matriz)
print("")
print("¿El cuadrado es mágico?", check_magico(matriz, n))
