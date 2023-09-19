num1 = int(input("Ingresá un primer número: "))
num2 = int(input("Ingresá un segundo número: "))
while True:
    opc = int(input("Ingresá una opción:\n1 - Sumar\n2 - Restar\n3 - Multiplicar\n4 - Dividir\n5 - Salir\n"))
    if opc == 1:
        suma = num1 + num2
        print("El resultado es ", suma)
    elif opc == 2:
        resta = num1 - num2
        print("El resultado es ", resta)
    elif opc == 3:
        multiplicacion = num1 * num2
        print("El resultado es ", multiplicacion)
    elif opc == 4:
        division = num1 / num2
        print("El resultado es ", division)
    elif opc == 5:
        resp = input("Estás seguro que querés salir del programa?: ")
        if resp == "si":
            print("Gracias por utilizar el programa")
            break
    else:
        print("La opción ingresada no corresponde a las ofrecidas")
