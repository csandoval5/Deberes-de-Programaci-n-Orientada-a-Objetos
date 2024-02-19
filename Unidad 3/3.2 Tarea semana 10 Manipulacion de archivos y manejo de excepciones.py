class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y setters


class Inventario:
    def __init__(self):
        self.productos = {}

    def cargar_inventario_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                for linea in f:
                    valores = linea.strip().split(',')
                    if len(valores) == 4:
                        id, nombre, cantidad, precio = valores
                        producto = Producto(id, nombre, int(cantidad), float(precio))
                        self.productos[id] = producto
                    else:
                        print(f"La línea '{linea.strip()}' no tiene el formato esperado y fue omitida.")
        except FileNotFoundError:
            print(f"El archivo {archivo} no existe. No se cargó ningún inventario.")
        except PermissionError:
            print(f"No se tienen permisos para acceder al archivo {archivo}. No se cargó ningún inventario.")

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto
        print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("El producto con el ID especificado no existe en el inventario.")

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos.values():
                print(f"ID: {producto.id}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

    def buscar_producto(self, nombre):
        productos_encontrados = []
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                productos_encontrados.append(producto)
        return productos_encontrados

    # Resto de métodos de la clase Inventario

# Interfaz de usuario en la consola
def menu():
    inventario = Inventario()
    inventario.cargar_inventario_desde_archivo("inventario.txt")  # Cargamos el inventario al iniciar el programa
    while True:
        print("\n1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar productos")
        print("6. Salir")

        opcion = input("\nElige una opción: ")

        if opcion == '1':
            id = input("Introduce el ID del producto: ")
            nombre = input("Introduce el nombre del producto: ")
            cantidad = int(input("Introduce la cantidad del producto: "))
            precio = float(input("Introduce el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            id = input("Introduce el ID del producto que quieres eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == '3':
            id = input("Introduce el ID del producto que quieres actualizar: ")
            cantidad = int(input("Introduce la nueva cantidad del producto: "))
            precio = float(input("Introduce el nuevo precio del producto: "))
            inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == '4':
            nombre = input("Introduce el nombre del producto que quieres buscar: ")
            productos = inventario.buscar_producto(nombre)
            if productos:
                for producto in productos:
                    print(f"ID: {producto.id}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
            else:
                print("No se encontraron productos con ese nombre.")
        elif opcion == '5':
            inventario.mostrar_productos()
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


menu()