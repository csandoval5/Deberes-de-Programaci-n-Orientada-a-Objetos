# Unidad 1
# Tarea Semana 2
# Abstracción
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

# Encapsulación
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.__raza = raza  # variable privada

    def get_raza(self):  # método getter para acceder a la variable privada
        return self.__raza

    def hablar(self):  # implementación del método hablar para Perro
        print(f"{self.nombre} hace woof!")

# Herencia
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def hablar(self):  # implementación del método hablar para Gato
        print(f"{self.nombre} hace miau!")

# Polimorfismo
def hacer_hablar(animal):
    animal.hablar()

perro = Perro("Fido", "Labrador")
gato = Gato("Tomas", "Blanco")

hacer_hablar(perro)  # Fido hace woof!
hacer_hablar(gato)  # Tomas hace miau!