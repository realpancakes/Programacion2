import random
class Juego:
    def __init__(self, nv):
        self.nv = nv
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
    def validaNumero(self, n):
        return 0 <= n <= 10
    def juega(self):
        self.reiniciaPartida()
        self.na = random.randint(0, 10)    
        while True:
            n = int(input("adivina entre 0 y 10: "))
            if not self.validaNumero(n):
                print("debe ser entre 0 y 10")
                continue
            if n == self.na:
                print("¡acertaste!")
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
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, n):
        if not (0 <= n <= 10):
            return False
        if n % 2 != 0:
            print("el numero debe ser par")
            return False
        return True
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, n):
        if not (0 <= n <= 10):
            return False
        if n % 2 == 0:
            print("el numero debe ser impar")
            return False
        return True
    
j1 = JuegoAdivinaNumero(3)
j2 = JuegoAdivinaPar(3)
j3 = JuegoAdivinaImpar(3)

j1.juega()
j2.juega()
j3.juega()