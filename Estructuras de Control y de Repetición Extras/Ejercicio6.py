cont = 0
cont1 = 0
cont2 = 0
suma1 = 0
suma2 = 0
while True:
    num = int(input("Ingresá un número: "))
    if num % 5 == 0:
        break
    if num % 2 == 0 and num >= 0:
        cont1 += 1
        suma1 += num
    elif num % 2 != 0 and num >= 0:
        cont2 += 1
        suma2 += num
    cont += 1
print("Total de números leídos: ", cont)
print("Total de números pares leídos: ", cont1)
print("Resultado de la sumatoria entre números pares: ", suma1)
print("Total de números impares leídos: ", cont2)
print("Resultado de la sumatoria entre números impares: ", suma2)
