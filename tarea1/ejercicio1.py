class Anime:

    def __init__(self, nom, gen, ep):
        self.nombre = nom
        self.genero = gen
        self.episodios = ep

    def __str__(self):
        return f"Nombre: {self.nombre}, Género: {self.genero}, Episodios: {self.episodios}"


# Prueba
a1 = Anime("dragon bal", "Acción", 100)
a2 = Anime("deat not", "misterio", 50)

print(a1)
print(a2)