import pickle

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def actualizar(self, cantidad=None, precio=None):
        if cantidad is not None:
            self.cantidad = cantidad
        if precio is not None:
            self.precio = precio

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("El producto con el ID dado no existe en el inventario.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            producto.actualizar(cantidad, precio)
        else:
            print("El producto con el ID dado no existe en el inventario.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values() if producto.nombre == nombre]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con el nombre dado.")

    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.productos, f)

    def cargar_inventario(self, filename):
        try:
            with open(filename, 'rb') as f:
                self.productos = pickle.load(f)
        except FileNotFoundError:
            print("El archivo de inventario no existe.")
        except Exception as e:
            print("Error al cargar el inventario:", e)


def menu():
    print("\nMenú:")
    print("1. Agregar nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto")
    print("4. Buscar y mostrar productos por nombre")
    print("5. Mostrar todos los productos en el inventario")
    print("6. Guardar inventario en archivo")
    print("7. Cargar inventario desde archivo")
    print("8. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


def main():
    inventario = Inventario()

    while True:
        opcion = menu()

        if opcion == "1":
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == "3":
            id = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (deje vacío para mantener): ")
            precio = input("Ingrese nuevo precio (deje vacío para mantener): ")
            if cantidad:
                cantidad = int(cantidad)
            if precio:
                precio = float(precio)
            inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)
        elif opcion == "5":
            inventario.mostrar_inventario()
        elif opcion == "6":
            filename = input("Ingrese el nombre del archivo para guardar el inventario: ")
            inventario.guardar_inventario(filename)
        elif opcion == "7":
            filename = input("Ingrese el nombre del archivo para cargar el inventario: ")
            inventario.cargar_inventario(filename)
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()