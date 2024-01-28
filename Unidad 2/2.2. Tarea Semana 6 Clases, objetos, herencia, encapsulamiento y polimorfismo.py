#Unidad 2
# Tarea Semana 6
# Definición de la clase base 'Animal'
class Animal:
    def __init__(self, especie, edad):
        self._especie = especie
        self._edad = edad

    # Implementación de encapsulación
    @property
    def especie(self):
        return self._especie

    @property
    def edad(self):
        return self._edad

    # Implementación de polimorfismo mediante sobrescritura
    def hablar(self):
        raise NotImplementedError("La clase base no implementa este método")


# Definición de la clase derivada 'Perro'
class Perro(Animal):
    def __init__(self, especie, edad, raza):
        super().__init__(especie, edad)
        self._raza = raza

    # Implementación de polimorfismo mediante sobrescritura
    def hablar(self):
        return "Guau, soy un perro."


# Definición de la clase derivada 'Gato'
class Gato(Animal):
    def __init__(self, especie, edad, color):
        super().__init__(especie, edad)
        self._color = color

    # Implementación de polimorfismo mediante sobrescritura
    def hablar(self):
        return "Miau, soy un gato."


# Creación de objetos de las clases 'Perro' y 'Gato'
perro = Perro("Canino", 5, "Bulldog")
gato = Gato("Felino", 3, "Negro")

# Uso de los métodos polimórficos 'hablar' y las propiedades 'especie' y 'edad'
print(perro.hablar())
print(gato.hablar())
print(perro.especie)
print(gato.edad)