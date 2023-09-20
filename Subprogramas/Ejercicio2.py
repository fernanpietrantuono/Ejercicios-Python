def mostrar_info():
    while True:
        name = input("Ingresá tu nombre: ")
        age = int(input("Ingresá tu edad: "))
        mayor_de_edad = age >= 18
        print(name, "de", age, "años, ¿es mayor de edad?", mayor_de_edad)
        resp = input("¿Quéres seguir mostrando personas?: ")
        if resp == "no":
            break


mostrar_info()
