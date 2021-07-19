class Animal():
    def __init__(self, nombre, edad,salud,felicidad):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.felicidad = felicidad
    def display_info(self):
        print(f"{self.nombre} tiene la salud: {self.salud} y el nivel de felicidad es {self.felicidad}")
        return self