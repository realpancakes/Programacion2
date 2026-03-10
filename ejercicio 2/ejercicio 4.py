class Bus:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = 0
        self.precio = 1.50
    def subir(self, cantidad):
        if self.pasajeros + cantidad <= self.capacidad:
            self.pasajeros += cantidad
            print(f"Subieron {cantidad} pasajeros")
        else:
            print("No hay suficientes asientos")
    def cobrar(self):
        total = self.pasajeros * self.precio
        print(f"Cobro total: Bs. {total}")
        return total
    def asientos_libres(self):
        libres = self.capacidad - self.pasajeros
        print(f"Asientos libres: {libres}")
        return libres
mi_bus = Bus(20)
mi_bus.subir(15)
mi_bus.cobrar()
mi_bus.asientos_libres()
mi_bus.subir(10)
mi_bus.asientos_libres()