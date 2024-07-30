num = int(input("Ingrese un tamaño para dibujar el cuadrado: "))
for i in range(num):
    for j in range(num):
        if j == num-1:
            print(" * ")
        elif i == 0 or i == num - 1:
            print(" * ", end="")
        elif 0 < j < num - 1:
            print("   ", end="")
        elif j == 0:
            print(" * ", end="")
    print("")
