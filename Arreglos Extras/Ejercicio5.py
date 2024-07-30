import random


def llenar_matriz(m, n_d):
    for i in range(n_d):
        for j in range(n_d):
            num = random.randint(0, 100)
            m.append(num)
    sumar_elementos(m, n_d)


def sumar_elementos(m, n_d):
    suma = 0
    print("")
    for i in range(n_d):
        for j in range(n_d):
            suma += m[i][j]
            print(m[i][j], " ", end="")
        print("")
    print("Tamaño de la matriz dimensionada:", n_d)
    print("El resultado de todos los elementos de la matriz es ", suma)


n = int(input("Dimensioná la matriz: "))
matriz = []
llenar_matriz(matriz, n)
