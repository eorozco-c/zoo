from animales import Animal

class Ave(Animal):
    def __init__(self, nombre, edad,salud = 100,felicidad = 50):
        super().__init__(nombre, edad,salud,felicidad)
    def alimentecion(self):
        self.salud += 9
        self.felicidad += 3
        return self
    def volar(self):
        print(f"{self.nombre} está volando")
