suma = 0
totalHijos = 0
sumaGeneral = 0
familias = int(input("Ingresá la cantidad de familias: "))
for i in range(1, familias + 1):
    hijos = int(input(f"Ingresá la cantidad de hijos para la familia {i}: "))
    totalHijos += hijos
    for j in range(1, hijos + 1):
        edad = int(input(f"Ingresá la edad del hijo {j}: "))
        suma += edad
sumaGeneral += suma
promedio = sumaGeneral / totalHijos
print("El promedio de edades de los hijos de todas las familias es", round(promedio))
