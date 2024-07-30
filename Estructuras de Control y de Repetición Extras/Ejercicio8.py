import random

num1 = random.randint(0, 10)
num2 = random.randint(0, 10)
respCorrecta = num1 * num2
while True:
    print(f"¿Cuánto es {num1} * {num2}?")
    try:
        resultado = int(input("Resultado: "))
    except ValueError:
        print("Por favor, ingresá números, no letras")
        continue
    if resultado == respCorrecta:
        print(f"Correcto!! Resultado: {num1} * {num2} = {respCorrecta}")
        break
    else:
        print("Incorrecto! Intentá otra vez.")
