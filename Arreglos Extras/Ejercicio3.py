import random


def llenar_vector(v, n_d):
    for i in range(n_d):
        num = random.randint(1, 100)
        v.append(num)
    mostrar_vector(v, n_d)


def mostrar_vector(v, n_d):
    print("")
    for i in range(n_d):
        print(f"[{v[i]}]", end="")
    print("")


n = int(input("Dimesioná el vector: "))
vector = []
llenar_vector(vector, n)
