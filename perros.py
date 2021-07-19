from animales import Animal

class Perro(Animal):
    def __init__(self, nombre, edad,salud = 90,felicidad = 70):
        super().__init__(nombre, edad,salud,felicidad)
    def alimentecion(self):
        self.salud += 3
        self.felicidad += 5
        return self

