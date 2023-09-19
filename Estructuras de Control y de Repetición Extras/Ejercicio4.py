cont1 = 0
cont2 = 0
suma1 = 0
suma2 = 0
n = int(input("Ingresá la cantidad de personas que querés promediar: "))
while cont2 < n:
    altura = float(input("Ingresá la altura: "))
    if altura < 1.60:
        suma1 += altura
        cont1 += 1
    suma2 += altura
    cont2 += 1
promedio1 = suma1 / cont1
promedio2 = suma2 / cont2
print("Promedio de personas menores de 1,60 m:", promedio1, "m")
print("Promedio general de estaturas:", promedio2, "m")
