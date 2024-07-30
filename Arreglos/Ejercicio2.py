import random


def llenar_vector(n):
    return [random.randint(1, 100) for _ in range(n)]


def buscar_numero(vector, numero):
    posiciones = []
    repeticiones = 0
    for i, elemento in enumerate(vector):
        if elemento == numero:
            posiciones.append(i)
            repeticiones += 1
    return posiciones, repeticiones


def main():
    n = int(input("Ingresá un tamaño para el vector: "))
    vector = llenar_vector(n)
    num_buscar = int(input("Ingresá el número a buscar en el vector: "))
    posiciones, repeticiones = buscar_numero(vector, num_buscar)
    if repeticiones > 0:
        print(f"El número {num_buscar} se encuentra en la/s posición/es:", posiciones)
        print(f"El número {num_buscar} se repite {repeticiones} vez/veces en el vector")
    else:
        print(f"El número {num_buscar} no se encuentra en el vector")


if __name__ == "__main__":
    main()
