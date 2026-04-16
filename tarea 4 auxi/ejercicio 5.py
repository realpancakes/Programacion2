from abc import ABC, abstractmethod
import math
class Figura(ABC):
    def __init__(self, color):
        self.color = color   
    @abstractmethod
    def obtenerArea(self):
        pass
class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.lado = lado 
    def obtenerArea(self):
        return self.lado * self.lado
class Triangulo(Figura):
    def __init__(self, color, lado1, lado2, lado3):
        super().__init__(color)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def obtenerArea(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
class Redondo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio
    def obtenerArea(self):
        return math.pi * self.radio * self.radio

c1 = Cuadrado("rojo", 5)
c2 = Cuadrado("azul", 7)
t1 = Triangulo("verde", 3, 4, 5)
t2 = Triangulo("amarillo", 6, 8, 10)
r1 = Redondo("negro", 4)
r2 = Redondo("blanco", 6)

print("=== cuadrados ===")
print(f"color: {c1.color}, area: {c1.obtenerArea()}")
print(f"color: {c2.color}, area: {c2.obtenerArea()}")
print("=== triangulos ===")
print(f"color: {t1.color}, area: {t1.obtenerArea()}")
print(f"color: {t2.color}, area: {t2.obtenerArea()}")
print("=== redondos ===")
print(f"color: {r1.color}, area: {r1.obtenerArea()}")
print(f"color: {r2.color}, area: {r2.obtenerArea()}")

area_c = c1.obtenerArea()
area_t = t1.obtenerArea()
if area_c > area_t:
    print(f"mayor area: cuadrado color {c1.color}")
elif area_t > area_c:
    print(f"mayor area: triangulo color {t1.color}")
else:
    print("areas iguales")