num = int(input("Ingresá un número: "))
char_sup2 = chr(0x00B2)
char_sup3 = chr(0x00B3)
raiz_cuadrada = "\u221A"
print(f"{num}{char_sup2} = {num ** 2}")
print(f"{num}{char_sup3} = {num ** 3}")
print(f"{raiz_cuadrada}{num} = {num**0.5}")
