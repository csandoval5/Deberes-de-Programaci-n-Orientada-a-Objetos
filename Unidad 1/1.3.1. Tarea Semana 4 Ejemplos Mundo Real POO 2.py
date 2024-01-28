#Unidad 1
# Tarea Semana 4 Parte 2
class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre

    def conducir(self, moto):
        if moto.encendida:
            print(f"{self.nombre} está conduciendo la moto {moto.marca} {moto.modelo}.")
        else:
            print(f"{self.nombre} no puede conducir porque la moto está apagada.")

class Moto1:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendida = False

    def encender(self):
        if not self.encendida:
            self.encendida = True
            print(f"La moto {self.marca} {self.modelo} está encendida.")
        else:
            print("La moto ya está encendida.")

    def apagar(self):
        if self.encendida:
            self.encendida = False
            print(f"La moto {self.marca} {self.modelo} está apagada.")
        else:
            print("La moto ya está apagada.")

class Moto2:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendida = False

    def encender(self):
        if not self.encendida:
            self.encendida = True
            print(f"La moto {self.marca} {self.modelo} está encendida.")
        else:
            print("La moto ya está encendida.")

    def apagar(self):
        if self.encendida:
            self.encendida = False
            print(f"La moto {self.marca} {self.modelo} está apagada.")
        else:
            print("La moto ya está apagada.")

# Crear instancias de la clase Conductor
conductor1 = Conductor("Juan")
conductor2 = Conductor("Ana")

# Crear instancias de las clases Moto1 y Moto2
mi_moto1 = Moto1("Honda", "CBR 600RR", "Rojo")
mi_moto2 = Moto2("Yamaha", "MT 07", "Negro")

# Encender las motos
mi_moto1.encender()
mi_moto2.encender()

# Los conductores intentan conducir las motos
conductor1.conducir(mi_moto1)
conductor2.conducir(mi_moto2)

# Apagar las motos
mi_moto1.apagar()
mi_moto2.apagar()

# Los conductores intentan conducir las motos nuevamente
conductor1.conducir(mi_moto1)
conductor2.conducir(mi_moto2)