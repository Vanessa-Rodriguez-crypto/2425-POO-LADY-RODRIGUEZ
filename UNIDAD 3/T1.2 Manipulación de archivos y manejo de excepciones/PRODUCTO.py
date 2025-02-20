import os


# Clase Producto que representa un artículo en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

    @staticmethod
    def from_string(data):
        id_producto, nombre, cantidad, precio = data.strip().split(',')
        return Producto(id_producto, nombre, int(cantidad), float(precio))


# Clase Inventario con manejo de archivos y excepciones
class Inventario:
    ARCHIVO = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID ya existe en el inventario.")
            return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        self.guardar_en_archivo()
        print("Producto eliminado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                self.guardar_en_archivo()
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados if resultados else "No se encontraron productos."

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)

    def guardar_en_archivo(self):
        try:
            with open(self.ARCHIVO, "w") as file:
                for producto in self.productos:
                    file.write(str(producto) + "\n")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")

    def cargar_desde_archivo(self):
        if not os.path.exists(self.ARCHIVO):
            return
        try:
            with open(self.ARCHIVO, "r") as file:
                self.productos = [Producto.from_string(line) for line in file.readlines()]
        except FileNotFoundError:
            print("Error: Archivo de inventario no encontrado. Se creará uno nuevo.")
        except ValueError:
            print("Error: Datos corruptos en el archivo. No se pudieron cargar los productos correctamente.")


def menu():
    inventario = Inventario()
    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: Entrada no válida. Asegúrese de ingresar números para cantidad y precio.")

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            try:
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("Error: Entrada no válida. Asegúrese de ingresar números para cantidad y precio.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if isinstance(resultados, list):
                for p in resultados:
                    print(p)
            else:
                print(resultados)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
