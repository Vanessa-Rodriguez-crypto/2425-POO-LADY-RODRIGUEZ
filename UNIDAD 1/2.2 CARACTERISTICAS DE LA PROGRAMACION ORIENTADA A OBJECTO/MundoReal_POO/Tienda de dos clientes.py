# Directorio: MundoReal_POO
# Programa: Sistema de reservas para una tienda con dos clientes

class Producto:
    """
    Clase que representa un producto en la tienda.
    Atributos:
        nombre: El nombre del producto.
        precio: El precio del producto.
    Métodos:
        mostrar_info: Muestra la información del producto.
    """
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        """
        Muestra la información del producto.
        """
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")


class Cliente:
    """
    Clase que representa a un cliente de la tienda.
    Atributos:
        nombre: El nombre del cliente.
        correo: El correo electrónico del cliente.
        historial_compras: Lista de productos comprados por el cliente.
    Métodos:
        agregar_compra: Agrega un producto al historial de compras.
        mostrar_historial: Muestra el historial de compras del cliente.
    """
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.historial_compras = []

    def agregar_compra(self, producto):
        """
        Agrega un producto al historial de compras del cliente.
        """
        self.historial_compras.append(producto)

    def mostrar_historial(self):
        """
        Muestra el historial de compras del cliente.
        """
        print(f"Historial de compras de {self.nombre}:")
        for producto in self.historial_compras:
            producto.mostrar_info()


class Reserva:
    """
    Clase que representa una reserva de un cliente.
    Atributos:
        cliente: El cliente que realiza la reserva.
        productos: Lista de productos reservados.
    Métodos:
        agregar_producto: Agrega un producto a la reserva.
        mostrar_reserva: Muestra los productos reservados por el cliente.
    """
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []

    def agregar_producto(self, producto):
        """
        Agrega un producto a la reserva.
        """
        self.productos.append(producto)

    def mostrar_reserva(self):
        """
        Muestra los productos reservados por el cliente.
        """
        print(f"Reserva de {self.cliente.nombre}:")
        for producto in self.productos:
            producto.mostrar_info()


# Creación de productos
producto1 = Producto("Camiseta", 15.99)
producto2 = Producto("Pantalones", 25.49)
producto3 = Producto("Zapatillas", 45.00)
producto4 = Producto("Chaqueta", 55.99)
producto5 = Producto("Sombrero", 12.00)

# Creación de clientes
cliente1 = Cliente("Fernando Torres", "fertorres123@gmail.com")
cliente2 = Cliente("Paula Carmona", "paula1547@gmail.com")

# Creación de reservas para los dos clientes
reserva1 = Reserva(cliente1)
reserva2 = Reserva(cliente2)

# Agregar productos a las reservas
reserva1.agregar_producto(producto1)
reserva1.agregar_producto(producto3)

reserva2.agregar_producto(producto2)
reserva2.agregar_producto(producto5)

# Mostrar las reservas
reserva1.mostrar_reserva()
reserva2.mostrar_reserva()

# Agregar productos al historial de compras de los clientes
cliente1.agregar_compra(producto1)
cliente1.agregar_compra(producto3)

cliente2.agregar_compra(producto2)
cliente2.agregar_compra(producto5)

# Mostrar los historiales de compras de los clientes
cliente1.mostrar_historial()
cliente2.mostrar_historial()
