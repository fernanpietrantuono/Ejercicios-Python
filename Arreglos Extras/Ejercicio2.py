import random


def vectores(v1, v2, n_d):
    igualdad = False
    for i_f in range(n_d):
        igualdad = v1 == v2
    return igualdad


n = int(input("Dimensioná los dos vectores: "))
vector1 = []
vector2 = []
for i in range(n):
    num1 = random.randint(0, 10)
    vector1.append(num1)
    num2 = random.randint(0, 10)
    vector2.append(num2)
for i in range(n):
    print(f"[{vector1[i]}]", end="")
print("")
for i in range(n):
    print(f"[{vector2[i]}]", end="")
print("")
print("¿Los elementos de ambos vectores son iguales?", vectores(vector1, vector2, n))
