a = int(input("Ingresá un número para el valor A: "))
b = int(input("Ingresá un número para el valor B: "))
c = int(input("Ingresá un número para el valor C: "))
d = int(input("Ingresá un número para el valor D: "))
print("Valor inicial de A:", a)
print("Valor inicial de B:", b)
print("Valor inicial de C:", c)
print("Valor inicial de D:", d)
aux = b
b = c
c = a
a = d
d = aux
print("----------------------------------------------------")
print("Valor final de A:", a)
print("Valor final de B:", b)
print("Valor final de C:", c)
print("Valor final de D:", d)
