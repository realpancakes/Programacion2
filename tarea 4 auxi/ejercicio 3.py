class Persona:
    def __init__(self, nombre, carnet, edad):
        self.nombre = nombre
        self.carnet = carnet
        self.edad = edad
    def mostrar(self):
        print(f"nombre: {self.nombre}, carnet: {self.carnet}, edad: {self.edad}")
class Estudiante(Persona):
    def __init__(self, nombre, carnet, edad, matricula, carrera):
        super().__init__(nombre, carnet, edad)
        self.matricula = matricula
        self.carrera = carrera 
    def mostrar(self):
        print(f"estudiante - nombre: {self.nombre}, carnet: {self.carnet}, edad: {self.edad}, matricula: {self.matricula}, carrera: {self.carrera}")   
    def misma_carrera(self, otro):
        return self.carrera == otro.carrera
class Docente(Persona):
    def __init__(self, nombre, carnet, edad, antiguedad, sueldo):
        super().__init__(nombre, carnet, edad)
        self.antiguedad = antiguedad
        self.sueldo = sueldo   
    def mostrar(self):
        print(f"docente - nombre: {self.nombre}, carnet: {self.carnet}, edad: {self.edad}, antiguedad: {self.antiguedad}, sueldo: {self.sueldo}")

e1 = Estudiante("ana lopez", 12345, 20, 2024001, "ingenieria")
e2 = Estudiante("carlos ruiz", 67890, 22, 2024002, "medicina")
d = Docente("maria gomez", 11111, 35, 10, 2500.50)

e1.mostrar()
e2.mostrar()
d.mostrar()

if e1.edad == d.edad:
    print(f"{e1.nombre} misma edad que docente")
if e2.edad == d.edad:
    print(f"{e2.nombre} misma edad que docente")
if e1.misma_carrera(e2):
    print("misma carrera")
else:
    print("diferente carrera")