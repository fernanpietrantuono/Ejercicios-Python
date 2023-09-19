def suma(n1, n2):
    return n1 + n2


def resta(n1, n2):
    return n1 - n2


def multiplicacion(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


num1 = int(input("Ingresá el primer número: "))
num2 = int(input("Ingresá el segundo número: "))
oper = input("¿Qué operación matemática querés realizar?: ")
if oper == "suma":
    resultado = suma(num1, num2)
    print("El resultado es", resultado)
elif oper == "resta":
    resultado = resta(num1, num2)
    print("El resultado es", resultado)
elif oper == "multiplicacion":
    resultado = multiplicacion(num1, num2)
    print("El resultado es", resultado)
elif oper == "division":
    resultado = division(num1, num2)
    print("El resultado es", resultado)
else:
    print("El dato introducido es incorrecto")
