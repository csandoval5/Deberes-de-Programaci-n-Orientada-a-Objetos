class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        print(f"Se ha creado el animal {self.nombre} de la especie {self.especie}")

    def __del__(self):
        print(f"El animal {self.nombre} de la especie {self.especie} ha sido eliminado")

# Ejemplo de uso
perro = Animal("Firulais", "Canino")
gato = Animal("Tom", "Felino")

# Se eliminan los objetos creados
del perro
del gato