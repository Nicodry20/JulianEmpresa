import math
nombre = input("ingrese nombre \n")
viajeros = int(input("ingrese la cantidad de viajeros \n"))
acompañantes = math.ceil (viajeros / 30) if viajeros > 0 else 0
precio = 500 * (viajeros + acompañantes)
print(f"{nombre}, habrá {acompañantes} acompañante(s) en el viaje.")
print(f"El costo total del viaje es: ${precio}")