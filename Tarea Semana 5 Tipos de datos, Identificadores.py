# Programa para calcular el area de un rectangulo

def calcular_area_rectangulo(longitud, ancho):
    area = longitud * ancho
    return area


def main():
    # Solicitamos al usuario que ingrese la longitud y el ancho del rectángulo
    longitud_str = input("Ingrese la longitud del rectángulo: ")
    ancho_str = input("Ingrese el ancho del rectángulo: ")

    # Convertimos las entradas a números de punto flotante (float)
    longitud = float(longitud_str)
    ancho = float(ancho_str)

    # Calculamos el área del rectángulo
    area_rectangulo = calcular_area_rectangulo(longitud, ancho)

    # Imprimir el resultado
    print(f"El área del rectángulo con longitud {longitud} y ancho {ancho} es: {area_rectangulo}")


if __name__ == "__main__":
    main()