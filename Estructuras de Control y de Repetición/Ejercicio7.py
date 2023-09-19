cont_correctas = 0
cont_incorrectas = 0
while True:
    cadena = input("Ingresá una cadena: ")
    if cadena == "&&&&&":
        break
    elif cadena.startswith("x") and cadena.endswith("o") and len(cadena) < 6:
        print("La cadena es correcta")
        cont_correctas += 1
    else:
        print("La cadena es incorrecta")
        cont_incorrectas += 1
print("Cadenas correctas leídas: ", cont_correctas)
print("Cadenas incorrectas leídas: ", cont_incorrectas)
