tiempo = int(input("Ingrese el tiempo en minutos: "))
dia = tiempo // 1440
hora = (tiempo // 60) - 24
print(tiempo, "minutos son", dia, "día/s y", hora, "hora/s")
