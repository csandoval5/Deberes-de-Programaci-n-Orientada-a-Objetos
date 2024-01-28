#Unidad 1
# Tarea Semana 3 Parte 2
# Implementación de un programa en Python para determinar el promedio semanal
# del clima  con programacion tradicional
def obtener_datos_diarios():
    """Obtiene la temperatura diaria de 7 días"""
    temperaturas = []
    for i in range(7):
        dia = input(f"Ingrese la temperatura del día {i+1}: ")
        temperaturas.append(float(dia))
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    """Calcula el promedio semanal de las temperaturas diarias"""
    return sum(temperaturas) / len(temperaturas)

# Ejecución
temperaturas = obtener_datos_diarios()
promedio = calcular_promedio_semanal(temperaturas)
print(f"El promedio semanal de las temperaturas es: {promedio}")