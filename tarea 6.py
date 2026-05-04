class Mueble:
    def __init__(self, tipo, material):
        self.__tipo = tipo
        self.__material = material
    def __str__(self):
        return f"Mueble [ Tipo: {self.__tipo}, Material: {self.__material} ]"
class Parqueo:
    def __init__(self, capacidad, precioH):
        self.__capacidad = capacidad
        self.__precioH = precioH
        self.__cantAuto = 0
        self.__placas = []
    def agregarAuto(self, placa):
        if self.__cantAuto < self.__capacidad:
            self.__placas.append(placa)
            self.__cantAuto += 1
            print(f"Auto {placa} agregado exitosamente")
        else:
            print("No hay capacidad disponible")
    def __str__(self):
        return f"Parqueo [ Capacidad: {self.__capacidad}, Autos: {self.__cantAuto} ]"

class Edificio:
    class Departamento:
        class Habitacion:
            def __init__(self, nombre, tamanio):
                self.__nombre = nombre
                self.__tamanio = tamanio
                self.__cantMuebles = 0
                self.__muebles = []
            def agregarMueble(self, mueble):
                if self.__cantMuebles < 100:
                    self.__muebles.append(mueble)
                    self.__cantMuebles += 1
            def getCantMuebles(self):
                return self.__cantMuebles
            def getNombre(self):
                return self.__nombre
            def __str__(self):
                return f"Habitación [ {self.__nombre}, Muebles: {self.__cantMuebles} ]"
        def __init__(self, nroPuerta, nroPiso):
            self.__nroPuerta = nroPuerta
            self.__nroPiso = nroPiso
            self.__nroHab = 0
            self.__hab = []
        def agregarHabitacion(self, nombre, tamanio):
            if self.__nroHab < 100:
                self.__hab.append(self.Habitacion(nombre, tamanio))
                self.__nroHab += 1
        def getHabitaciones(self):
            return self.__hab
        def getNroPuerta(self):
            return self.__nroPuerta
        def getNroPiso(self):
            return self.__nroPiso
        def getNroHab(self):
            return self.__nroHab
        def getTotalMuebles(self):
            return sum(h.getCantMuebles() for h in self.__hab)
        def __str__(self):
            return f"Departamento [ Puerta: {self.__nroPuerta}, Piso: {self.__nroPiso}, Habs: {self.__nroHab} ]"
    def __init__(self, nombre, superficie):
        self.__nombre = nombre
        self.__superficie = superficie
        self.__cantDep = 0
        self.__deps = []
        self.__parqueo = None 
    def agregarDepartamento(self, nroPuerta, nroPiso): 
        if self.__cantDep < 100:
            self.__deps.append(self.Departamento(nroPuerta, nroPiso))
            self.__cantDep += 1
    def agregarParqueo(self, parqueo): 
        self.__parqueo = parqueo
        print("Parqueo agregado exitosamente al edificio")
    def getDepartamentos(self):
        return self.__deps
    def getParqueo(self):
        return self.__parqueo
    def setDepartamentos(self, nuevos_deps):
        self.__deps = nuevos_deps
        self.__cantDep = len(nuevos_deps)
    def __str__(self):
        info_parqueo = self.__parqueo if self.__parqueo else "Sin parqueo"
        return f"Edificio {self.__nombre}\n  Deptos: {self.__cantDep}\n  {info_parqueo}"
def es_primo(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
print("--- EJECUCIÓN DEL SISTEMA ---")
print("\n Creando Edificio y agregando Parqueo")
edificio = Edificio("Los Pinos", 2500.5)
mi_parqueo = Parqueo(2, 15.0) 
edificio.agregarParqueo(mi_parqueo)
edificio.agregarDepartamento(101, 1)
edificio.agregarDepartamento(102, 1)
edificio.agregarDepartamento(201, 2)
deptos = edificio.getDepartamentos()
deptos[0].agregarHabitacion("Sala", 25.0)  
deptos[0].agregarHabitacion("Cuarto", 15.0) 
deptos[1].agregarHabitacion("Cocina", 12.0)
deptos[2].agregarHabitacion("Suite", 40.0)
y = 1
print(f"\n Departamento con más habitaciones en el piso {y}:")
deptos_piso_y = [d for d in edificio.getDepartamentos() if d.getNroPiso() == y]
if deptos_piso_y:
    max_habs = max(d.getNroHab() for d in deptos_piso_y)
    for d in deptos_piso_y:
        if d.getNroHab() == max_habs:
            print(d)
z, x = 101, 1
print(f"\n Agregando Mueble al Depto Puerta {z}, Piso {x}")
nuevo_mueble = Mueble("Sofá", "Cuero")
for d in edificio.getDepartamentos():
    if d.getNroPuerta() == z and d.getNroPiso() == x:
        habs = d.getHabitaciones()
        if habs:
            habs[0].agregarMueble(nuevo_mueble)
            print(f"Mueble agregado a: {habs[0].getNombre()}")
print("\n Departamento(s) con más muebles:")
todos_deptos = edificio.getDepartamentos()
if todos_deptos:
    max_muebles = max(d.getTotalMuebles() for d in todos_deptos)
    for d in todos_deptos:
        if d.getTotalMuebles() == max_muebles:
            print(d)
piso_z = 1
print(f"\n Habitación con más muebles en el piso {piso_z}:")
max_m = -1
hab_nombre = "Ninguna"
for d in edificio.getDepartamentos():
    if d.getNroPiso() == piso_z:
        for h in d.getHabitaciones():
            if h.getCantMuebles() > max_m:
                max_m = h.getCantMuebles()
                hab_nombre = h.getNombre()
print(hab_nombre)
print("\n Eliminando departamentos con cantidad prima de habitaciones")
deptos_filtrados = [d for d in edificio.getDepartamentos() if not es_primo(d.getNroHab())]
edificio.setDepartamentos(deptos_filtrados)
print(f"Departamentos restantes: {len(edificio.getDepartamentos())}")
print("\n Agregando autos al parqueo")
parqueo_actual = edificio.getParqueo()
if parqueo_actual:
    parqueo_actual.agregarAuto("ABC-123")
    parqueo_actual.agregarAuto("XYZ-987")
    parqueo_actual.agregarAuto("QQQ-000") 
print("\n--- ESTADO FINAL DEL EDIFICIO ---")
print(edificio)