tiempo = int(input("Ingresá el tiempo en minutos: "))
dia = tiempo // 1440
hora = (tiempo // 60) - 24
print(f"{tiempo} minutos son {dia} día/s y {hora} hora/s")
