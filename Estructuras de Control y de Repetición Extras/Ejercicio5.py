i = 0
suma = 0
valor_min = 1000
valor_max = 0
n = int(input("Ingresá el valor de N: "))
while i < n:
    num = int(input(f"Ingresá un número {i + 1}: "))
    if num < valor_min:
        valor_min = num
    elif num > valor_max:
        valor_max = num
    if num >= 0:
        suma += num
        i += 1
promedio = suma / n
print("El nuevo valor mínimo es", valor_min)
print("El nuevo valor máximo es", valor_max)
print(f"El promedio de {n} números es", promedio)
