import time
import random
class Cronometro:
    def __init__(self):
        self.__inicia = time.time()
        self.__finaliza = None
    def inicia(self):
        self.__inicia = time.time()
        self.__finaliza = None
    def detener(self):
        self.__finaliza = time.time()
    def lapsoDeTiempo(self):
        if self.__finaliza is None:
            return (time.time() - self.__inicia) * 1000
        return (self.__finaliza - self.__inicia) * 1000
    def get_inicia(self):
        return self.__inicia

    def get_finaliza(self):
        return self.__finaliza
def ordenacion_seleccion(lista):
    n = len(lista)
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
numeros = [random.randint(1, 1000000) for _ in range(10000)]
cron = Cronometro()
cron.inicia()
ordenacion_seleccion(numeros)
cron.detener()
print("Tiempo de ejecucion en milisegundos:", cron.lapsoDeTiempo())