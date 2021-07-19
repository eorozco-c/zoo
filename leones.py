from animales import Animal

class Leon(Animal):
    def __init__(self, nombre, edad,salud = 10,felicidad = 10):
        super().__init__(nombre, edad,salud,felicidad)
    def alimentecion(self):
        self.salud += 10
        self.felicidad += 5
        return self