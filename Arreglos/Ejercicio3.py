import random

n = int(input("Dimensioná el vector: "))
vector = [random.randint(1, 99999) for _ in range(n)]
contadores = [0, 0, 0, 0, 0]
for num in vector:
    digitos = len(str(num))
    if digitos <= 5:
        contadores[digitos - 1] += 1
print(vector, end="")
print("")
for i in range(5):
    print(f"Cantidad de números de {i + 1} dígito/s: {contadores[i]}")
