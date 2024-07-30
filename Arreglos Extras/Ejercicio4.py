alumnado = []
cont1 = 0
cont2 = 0
for i in range(10):
    print(f"Estudiante n° {i + 1}:")
    nota_tpe1 = float(input("Ingresá la nota del 1° Trabajo Práctico Evaluativo: "))
    nota_tpe2 = float(input("Ingresá la nota del 2° Trabajo Práctico Evaluativo: "))
    porcentaje_tpe1 = (nota_tpe1 * 10) / 10
    porcentaje_tpe2 = (nota_tpe1 * 15) / 10
    print(f"Calificación 1° TPE: {porcentaje_tpe1}%")
    print(f"Calificación 2° TPE: {porcentaje_tpe2}%")
    nota_parcial1 = float(input("Ingresá la nota del 1° parcial: "))
    nota_parcial2 = float(input("Ingresá la nota del 2° parcial: "))
    porcentaje_parcial1 = (nota_parcial1 * 25) / 10
    porcentaje_parcial2 = (nota_parcial1 * 50) / 10
    print(f"Calificación 1° parcial: {porcentaje_parcial1}%")
    print(f"Calificación 2° parcial: {porcentaje_parcial2}%")
    nota_total = (nota_tpe1 + nota_tpe2 + nota_parcial1 + nota_parcial2) / 4
    alumnado.append(nota_total)
    porcentaje_total = porcentaje_tpe1 + porcentaje_tpe2 + porcentaje_parcial1 + porcentaje_parcial2
    if alumnado[i] >= 7:
        cont1 += 1
    else:
        cont2 += 2
    print(f"\nCalificación final: {porcentaje_total}%\n")
print("Total alumnos aprobados:", cont1)
print("Total alumnos desaprobados:", cont2)
