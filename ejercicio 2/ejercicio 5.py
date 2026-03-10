class Jugador:
    def __init__(self, nombre, diamantes=0):
        self.nombre = nombre
        self.diamantes = diamantes
    def stacks(self):
        return self.diamantes // 64
    def __str__(self):
        return f"{self.nombre}: {self.diamantes} diamantes ({self.stacks()} stacks)"
class ServidorMinecraft:
    def __init__(self):
        self.jugadores = []
        self.max_jugadores = 10
    def agregar(self, nombre, diamantes):
        if len(self.jugadores) < self.max_jugadores:
            self.jugadores.append(Jugador(nombre, diamantes))
            print(f"✓ {nombre} agregado")
        else:
            print("✗ Servidor lleno")
    def verificar_stacks(self):
        for j in self.jugadores:
            print(f"{j.nombre}: {j.stacks()} stacks")
    def max_diamantes(self):
        if self.jugadores:
            max_j = max(self.jugadores, key=lambda j: j.diamantes)
            print(f"Más diamantes: {max_j.nombre} ({max_j.diamantes})")
    
    def total_diamantes(self):
        total = sum(j.diamantes for j in self.jugadores)
        print(f"Total diamantes: {total}")
        return total
server = ServidorMinecraft()
server.agregar("Steve", 128)
server.agregar("Alex", 65)
server.agregar("Creeper", 192)

print("\n--- Stacks ---")
server.verificar_stacks()

print("\n--- Estadísticas ---")
server.max_diamantes()
server.total_diamantes()