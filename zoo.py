from leones import Leon
from aves import Ave
from perros import Perro

class Zoo():
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name,edad):
        self.animals.append(Leon(name, edad))
    def add_dog(self, name, edad):
        self.animals.append(Perro(name, edad))
    def add_ave(self, name, edad):
        self.animals.append(Ave(name, edad))
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
    def alimentar(self, name):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            if animal.nombre == name:
                animal.alimentecion()
                print(f"Alimentando a {animal.nombre}")
                animal.display_info()
        return self
    def volar_ave(self, name):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            if animal.nombre == name:
                animal.volar()
        return self

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Mufasa", 15)
zoo1.add_dog("Rex", 3)
zoo1.add_ave("Pajarraco",2)
zoo1.print_all_info()
zoo1.alimentar("Rex")
zoo1.print_all_info()
zoo1.volar_ave("Pajarraco")
