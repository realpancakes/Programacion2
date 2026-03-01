class Televisor:
    def __init__(self, mar="Sin marca", res=480, tip="LED"):
        self.marca = mar
        self.resolucion = res
        self.tipo = tip

    def __str__(self):
        return f"Marca: {self.marca}, Resolución: {self.resolucion}, Tipo: {self.tipo}"



t1 = Televisor("Samsung", 4, "OLED")
t2 = Televisor()  # Constructor vacío

print(t1)
print(t2)