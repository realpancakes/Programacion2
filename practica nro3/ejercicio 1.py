import random
class Juego:
    def __init__(self, nrovidas):
        self.nv = nrovidas
        self.r = 0
    def reiniciaPartida(self):
        self.nv = self.nv
    def actualizaRecord(self):
        self.r =self.r+1
    def quitaVida(self):
        self.nv =self.nv-1
        return self.nv > 0
class JuegoAdivinaNumero(Juego):
    def __init__(self, nv):
        super().__init__(nv)
        self.na = 0
    def juega(self):
        self.reiniciaPartida()
        self.na = random.randint(0, 10)
        while True:
            n = int(input("Adivina un numero entre 0 y 10: "))
            if n == self.na:
                print("¡Acertaste!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if n < self.na:
                        print("el numero es mayor")
                    else:
                        print("el numero es menor")
                else:
                    print("sin vidas")
                    break

j = JuegoAdivinaNumero(3)
j.juega()