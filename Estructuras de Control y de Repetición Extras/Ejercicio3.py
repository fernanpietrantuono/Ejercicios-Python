importe = 0
socio = input("Ingresá el tipo de clase de socio: ")
socio.upper()
costo = float(input("Ingresá el precio de tu tratamiento: "))
if socio == "A":
    importe = costo - (costo * 50) / 100
elif socio == "B":
    importe = costo - (costo * 35) / 100
elif socio == "C":
    importe = costo
else:
    print("La letra ingresada no corresponde al tipo de socio")
print("El importe es de $", importe)
