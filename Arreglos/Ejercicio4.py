import random


def generar_elementos_aleatorios(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.randint(-10, 10))
        matriz.append(fila)
    return matriz


def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()


def crear_matriz_traspuesta(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    traspuesta = [[0] * filas for _ in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            traspuesta[j][i] = matriz[i][j]
    return traspuesta


matriz_original = generar_elementos_aleatorios(4, 4)
print("Matriz Original:")
mostrar_matriz(matriz_original)
matriz_traspuesta = crear_matriz_traspuesta(matriz_original)
print("\nMatriz Traspuesta:")
mostrar_matriz(matriz_traspuesta)
