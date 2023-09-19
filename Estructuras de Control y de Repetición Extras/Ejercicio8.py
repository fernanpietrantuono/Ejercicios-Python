import random

num1 = random.randint(0, 10)
num2 = random.randint(0, 10)
multiplicacion = int(input("Ingresá un resultado para adivinar la multiplicación: "))
respCorrecta = num1 * num2
while multiplicacion != respCorrecta:
    multiplicacion = input("Incorrecto. Ingresá nuevamente: ")
print("Correcto!!!!!! La respuesta correcta es", respCorrecta)
