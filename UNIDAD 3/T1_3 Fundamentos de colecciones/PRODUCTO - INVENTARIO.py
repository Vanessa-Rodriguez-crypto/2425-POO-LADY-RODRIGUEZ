import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def obtener_info(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        if id_producto in self.productos:
            print("Error: El ID ya existe en el inventario.")
        else:
            self.productos[id_producto] = Producto(id_producto, nombre, cantidad, precio)
            self.guardar_en_archivo()
            print("Producto agregado con éxito.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado con éxito.")
        else:
            print("Error: No se encontró el producto.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].actualizar_precio(nuevo_precio)
            self.guardar_en_archivo()
            print("Producto actualizado con éxito.")
        else:
            print("Error: No se encontró el producto.")

    def buscar_producto(self, nombre):
        encontrados = [p.obtener_info() for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if encontrados:
            print("\n".join(encontrados))
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto.obtener_info())
        else:
            print("El inventario está vacío.")

    def guardar_en_archivo(self):
        with open("inventario.json", "w") as archivo:
            json.dump({id: vars(prod) for id, prod in self.productos.items()}, archivo, indent=4)

    def cargar_desde_archivo(self):
        try:
            with open("inventario.json", "r") as archivo:
                datos = json.load(archivo)
                self.productos = {id: Producto(**info) for id, info in datos.items()}
        except FileNotFoundError:
            self.productos = {}


def menu():
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            inventario.agregar_producto(id_producto, nombre, cantidad, precio)
        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje vacío si no desea cambiar): ")
            precio = input("Nuevo precio (deje vacío si no desea cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "5":
            inventario.mostrar_inventario()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    menu()
