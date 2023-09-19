def division(num1, num2):
    cont = 0
    while True:
        cont += 1
        if num1 > num2:
            num1 -= num2
        print("Resto: ", num1)
        print("Cociente ", cont)
        if num2 > num1:
            break


n1 = int(input("Ingresá un primer número: "))
n2 = int(input("Ingresá un primer número: "))
division(n1, n2)
