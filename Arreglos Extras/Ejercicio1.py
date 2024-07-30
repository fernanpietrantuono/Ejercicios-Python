suma = 0
n = int(input("Dimensioná el tamaño del vector: "))
vector = []
for i in range(n):
    num = int(input(f"Ingresá el {i + 1}° número: "))
    vector.append(num)
    suma += vector[i]
print("El resultado es", suma)
