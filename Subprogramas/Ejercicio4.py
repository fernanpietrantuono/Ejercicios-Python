def num_primo(n):
    cont = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cont += 1
    primos = cont == 2
    return primos


num = int(input("Ingresá un número: "))
respuesta = num_primo(num)
print("¿El", num, "es un número primo?", respuesta)
