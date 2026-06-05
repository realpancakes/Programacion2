class SueldoInvalidoException(Exception):
    def __init__(self, mensaje="sueldo menor al minimo legal de 2500 bs"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
class CargoInvalidoException(Exception):
    def __init__(self, mensaje="el cargo no puede contener numeros, solo letras"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
class Empleado:
    def __init__(self, nombre: str, cargo: str, sueldo: float):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo
    def __str__(self):
        return f"nombre: {self.nombre}, cargo: {self.cargo}, sueldo: {self.sueldo:.2f} bs"
class Empresa:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.empleados = []
    def registrar_empleado(self, empleado: Empleado):
        self.empleados.append(empleado)
    def mostrar_planilla(self):
        print(f"\n planilla de la empresa: {self.nombre.upper()} ")
        if len(self.empleados) == 0:
            print("no hay empleados registrados,")
            return    
        for i in range(len(self.empleados)):
            print(f"[{i}] {self.empleados[i]}")
def solicitar_cargo():
    while True:
        try:
            cargo = input("ingrese el cargo del empleado: ").strip()
            if any(char.isdigit() for char in cargo) or cargo == "":
                raise CargoInvalidoException()
            return cargo
        except CargoInvalidoException as e:
            print(f"[error] {e}, intente de nuevo,")
def solicitar_sueldo():
    while True:
        try:
            sueldo_input = input("ingrese el sueldo del empleado (bs): ")
            sueldo = float(sueldo_input)            
            if sueldo < 2500:
                raise SueldoInvalidoException()
            return sueldo            
        except ValueError:
            print("[error] ingrese un monto numerico valido,")
        except SueldoInvalidoException as e:
            print(f"[aviso] {e},")
            print("-> se asigno automaticamente el salario minimo de 2500 bs,")
            return 2500.0
if __name__ == "__main__":
    print("sistema de recursos humanos")
    nombre_empresa = input("ingrese el nombre de la empresa: ")
    mi_empresa = Empresa(nombre_empresa)
    while True:
        print("\n registro de nuevo empleado")
        nombre = input("ingrese el nombre (o 'salir' para terminar): ").strip()
        if nombre.lower() == 'salir':
            break
        cargo = solicitar_cargo()
        sueldo = solicitar_sueldo()
        nuevo_empleado = Empleado(nombre, cargo, sueldo)
        mi_empresa.registrar_empleado(nuevo_empleado)
        print(f"empleado {nombre} registrado,")
    mi_empresa.mostrar_planilla()