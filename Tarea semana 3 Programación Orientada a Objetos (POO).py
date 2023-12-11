# Implementación de un programa en Python para determinar el promedio
# semanal del clima con programacion orientada a objetos POO
class DatosClima:
    def __init__(self):
        self.temperaturas = []

    def obtener_datos_diarios(self):
        """Obtiene la temperatura diaria de 7 días"""
        for i in range(7):
            dia = input(f"Ingrese la temperatura del día {i+1}: ")
            self.temperaturas.append(float(dia))

    def calcular_promedio_semanal(self):
        """Calcula el promedio semanal de las temperaturas diarias"""
        return sum(self.temperaturas) / len(self.temperaturas)

# Ejecución
datos_clima = DatosClima()
datos_clima.obtener_datos_diarios()
promedio = datos_clima.calcular_promedio_semanal()
print(f"El promedio semanal de las temperaturas es: {promedio}")