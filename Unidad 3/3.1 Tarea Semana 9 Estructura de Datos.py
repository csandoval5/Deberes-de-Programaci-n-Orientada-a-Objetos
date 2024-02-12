#Tarea Semana 9 Estructura de datos
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.get_id() not in self.productos:
            self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id].set_precio(precio)

    def buscar_producto(self, nombre):
        return [producto for producto in self.productos.values() if nombre.lower() in producto.get_nombre().lower()]

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")


# Interfaz de usuario en la consola
def menu():
    inventario = Inventario()
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
            for producto in productos:
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
        elif opcion == '5':
            inventario.mostrar_productos()
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    menu()