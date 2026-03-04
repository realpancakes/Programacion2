class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def __determinante(self):
        return self.__a * self.__d - self.__b * self.__c
    def tieneSolucion(self):
        return self.__determinante() != 0
    def getX(self):
        if self.tieneSolucion():
            return (self.__e * self.__d - self.__b * self.__f) / self.__determinante()
        else:
            return None
    def getY(self):
        if self.tieneSolucion():
            return (self.__a * self.__f - self.__e * self.__c) / self.__determinante()
        else:
            return None
print("Ingrese a, b, c, d, e, f:")
valores = list(map(float, input().split()))
a, b, c, d, e, f = valores
ecuacion = EcuacionLineal(a, b, c, d, e, f)
if ecuacion.tieneSolucion():
    print("x =", ecuacion.getX(), ", y =", ecuacion.getY())
else:
    print("La ecuacion no tiene solucion")