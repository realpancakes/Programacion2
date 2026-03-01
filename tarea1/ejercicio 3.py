class Instrumento:

    def __init__(self, nom, mat, tip):
        self.__nombre = nom
        self.__material = mat
        self.__tipo = tip

  
    def get_nombre(self):
        return self.__nombre

    def get_material(self):
        return self.__material

    def get_tipo(self):
        return self.__tipo

    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_material(self, material):
        self.__material = material

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def __str__(self):
        return f"Nombre: {self.__nombre}, Material: {self.__material}, Tipo: {self.__tipo}"



a1 = Instrumento("Guitarra", "Madera", "Cuerda")

print(a1)                 
print(a1.get_nombre())    

a1.set_nombre("Piano")     
print(a1)