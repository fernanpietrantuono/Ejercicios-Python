for i in range(10):
    if i == 3:
        letra1 = "E"
    else:
        letra1 = str(i)
    for j in range(10):
        if j == 3:
            letra2 = "E"
        else:
            letra2 = str(j)
        for k in range(10):
            if k == 3:
                letra3 = "E"
            else:
                letra3 = str(k)
            print(letra1, "-", letra2, "-", letra3)
        print("")
