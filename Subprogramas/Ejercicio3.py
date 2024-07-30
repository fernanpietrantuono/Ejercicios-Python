def cambio_moneda(eur, mon):
    if mon == "dolares":
        dolares = eur * 1.28611
        print(f"{eur}€ son ${dolares}")
    elif mon == "yenes":
        yenes = eur * 129.852
        print(f"{eur}€ son ¥{yenes}")
    elif mon == "libras":
        libras = eur * 0.86
        print(f"{eur}€ son £{libras}")
    else:
        print("Lo siento, no se encuentra dentro de estas opciones")


euros = float(input("Ingresá el monto en euros: "))
moneda = input("Ingresá una moneda a convertir: ")
cambio_moneda(euros, moneda)
