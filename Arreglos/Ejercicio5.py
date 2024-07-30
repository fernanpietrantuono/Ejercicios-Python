# Función para verificar si una matriz es antisimétrica
def es_antisimetrica(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    # Comprobar si la matriz es cuadrada
    if filas != columnas:
        return False

    # Calcular la traspuesta de la matriz
    traspuesta = [[0] * filas for _ in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            traspuesta[j][i] = matriz[i][j]
    print("Matriz Traspuesta:")
    mostrar_matriz(traspuesta)

    # Verificar si la matriz es igual a la traspuesta cambiada de signo
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] != -traspuesta[i][j]:
                return False

    return True


def mostrar_matriz(matriz):
    for fila_f2 in matriz:
        for elemento in fila_f2:
            print(elemento, end="\t")
        print()


n = int(input("Dimensioná las matrices: "))
matriz_or = []
for i_o in range(n):
    fila = []
    for j_o in range(n):
        num = int(input(f"Ingresá un valor para la posición {i_o},{j_o}: "))
        fila.append(num)
    matriz_or.append(fila)
print("Matriz Original:")
mostrar_matriz(matriz_or)
print("¿Las matrices son asimétricas?", es_antisimetrica(matriz_or))
