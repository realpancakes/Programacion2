import math
def promedio(valores):
    return sum(valores) / len(valores)
def desviacion(valores):
    prom = promedio(valores)
    suma = 0
    for x in valores:
        suma += (x - prom) ** 2
    return math.sqrt(suma / (len(valores) - 1))
numeros = list(map(float, input("Ingrese 10 numeros: ").split()))
prom = promedio(numeros)
desv = desviacion(numeros)
print("El promedio es", round(prom, 2))
print("La desviacion estandar es", round(desv, 5))
numeros = list(map(float, input("Ingrese 10 numeros: ").split()))
estad = Estadistica(numeros)
print("El promedio es", round(estad.promedio(), 2))
print("La desviacion estandar es", round(estad.desviacion(), 5))