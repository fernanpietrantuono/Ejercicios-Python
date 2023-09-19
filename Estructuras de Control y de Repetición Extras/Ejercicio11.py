def escalera(n):
    acum = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            acum = j + acum
            if j != 1:
                print(j, end="")
            else:
                print(j, end="")
        print("")


num = int(input("Ingresá un número para armar la escalera: "))
escalera(num)
