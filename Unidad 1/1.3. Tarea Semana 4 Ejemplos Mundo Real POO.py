# Unidad 1
# Tarea Semana 4 Parte 1
class Moto:
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

mi_moto = Moto("Honda", "CBR 600RR", "Rojo")
mi_moto.encender()
mi_moto.apagar()