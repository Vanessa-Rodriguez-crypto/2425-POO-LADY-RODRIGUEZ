# Clase Producto que representa un artículo en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Se inicializan los atributos del producto
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos getter para acceder a los atributos del producto
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos setter para modificar la cantidad y el precio del producto
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Método para representar el producto en formato de cadena
    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


# Clase Inventario que gestiona una colección de productos
class Inventario:
    def __init__(self):
        # Se inicializa la lista de productos
        self.productos = []

    # Método para agregar un producto al inventario
    def agregar_producto(self, producto):
        # Se verifica si el ID del producto ya existe en el inventario
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID ya existe en el inventario.")
                return
        # Se agrega el producto a la lista
        self.productos.append(producto)
        print("Producto agregado exitosamente.")

    # Método para eliminar un producto por su ID
    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        print("Producto eliminado.")

    # Método para actualizar la cantidad o el precio de un producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    # Método para buscar productos por nombre (puede haber múltiples coincidencias)
    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados if resultados else "No se encontraron productos."

    # Método para mostrar todos los productos del inventario
    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)


# Función que maneja la interfaz de usuario en la consola
def menu():
    inventario = Inventario()
    while True:
        # Se muestra el menú de opciones
        print("\nSistema de Gestión de Inventarios")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        # Opción para agregar un nuevo producto
        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        # Opción para eliminar un producto por ID
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        # Opción para actualizar la cantidad o el precio de un producto
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        # Opción para buscar productos por nombre
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if isinstance(resultados, list):
                for p in resultados:
                    print(p)
            else:
                print(resultados)

        # Opción para mostrar todos los productos
        elif opcion == "5":
            inventario.mostrar_productos()

        # Opción para salir del programa
        elif opcion == "6":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu()
