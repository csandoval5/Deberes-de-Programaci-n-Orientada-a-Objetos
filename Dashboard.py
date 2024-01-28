import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': [
            'Unidad 1/1.1. Tarea semana 2 Desarrollo de Ejemplos de Técnicas de Programación (POO).py',
            'Unidad 1/1.2. Tarea semana 3 Programación Orientada a Objetos (POO).py',
            'Unidad 1/1.2.1. Tarea semana 3 Programación Tradicional.py',
            'Unidad 1/1.3. Tarea Semana 4 Ejemplos Mundo Real POO.py',
            'Unidad 1/1.3.1. Tarea Semana 4 Ejemplos Mundo Real POO 2.py',
        ],
        '2': [
            'Unidad 2/2.1. Tarea Semana 5 Tipos de datos, Identificadores.py',
            'Unidad 2/2.2. Tarea Semana 6 Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
            'Unidad 2/2.3. Tarea semana 7 Constructores y Destructores.py',
            # Agrega aquí el resto de las rutas de los scripts
        ],
        # Agrega aquí el resto de las claves y rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key][0].split('/')[0]}")
        print("0 - Salir")

        eleccion = input("Elige una unidad para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Muestra cada script de la unidad seleccionada
            for ruta_script in opciones[eleccion]:
                # Asegura que el path sea absoluto
                ruta_completa = os.path.join(ruta_base, ruta_script)
                mostrar_codigo(ruta_completa)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()