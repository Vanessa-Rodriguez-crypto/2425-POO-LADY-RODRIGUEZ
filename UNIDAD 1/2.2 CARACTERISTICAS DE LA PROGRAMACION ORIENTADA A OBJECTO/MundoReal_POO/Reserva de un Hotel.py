# Clase que representa a un Huésped
class Huesped:
    def __init__(self, nombre, dni):
        """
        Inicializa un huésped con su nombre y número de identificación (DNI).
        """
        self.nombre = nombre
        self.dni = dni

    def __str__(self):
        """
        Retorna una representación en cadena del huésped.
        """
        return f"Huésped: {self.nombre}, DNI: {self.dni}"

# Clase que representa a una Habitación
class Habitacion:
    def __init__(self, numero, tipo, precio_noche):
        """
        Inicializa una habitación con su número, tipo (individual, doble, suite) y precio por noche.
        """
        self.numero = numero
        self.tipo = tipo
        self.precio_noche = precio_noche
        self.disponible = True  # Inicialmente la habitación está disponible

    def reservar(self):
        """
        Marca la habitación como no disponible.
        """
        if self.disponible:
            self.disponible = False
            print(f"Habitación {self.numero} reservada exitosamente.")
        else:
            print(f"Habitación {self.numero} no está disponible.")

    def liberar(self):
        """
        Marca la habitación como disponible.
        """
        self.disponible = True
        print(f"Habitación {self.numero} ahora está disponible.")

    def __str__(self):
        """
        Retorna una representación en cadena de la habitación.
        """
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Habitación {self.numero} ({self.tipo}), Precio por noche: {self.precio_noche} - Estado: {estado}"

# Clase que representa una Reserva
class Reserva:
    def __init__(self, huesped, habitacion, noches):
        """
        Inicializa una reserva con un huésped, una habitación y el número de noches.
        """
        self.huesped = huesped
        self.habitacion = habitacion
        self.noches = noches

    def calcular_precio_total(self):
        """
        Calcula el precio total de la reserva.
        """
        return self.habitacion.precio_noche * self.noches

    def __str__(self):
        """
        Retorna una representación en cadena de la reserva.
        """
        return f"Reserva para {self.huesped}\n{self.habitacion}\nDuración: {self.noches} noches\nPrecio total: {self.calcular_precio_total()}"

# Ejemplo de uso
if __name__ == "__main__":
    # Creando instancias de los objetos
    huesped1 = Huesped("Jenniffer Rodriguez", "2150231547")
    habitacion1 = Habitacion(101, "Individual", 50)
    habitacion2 = Habitacion(102, "Doble", 80)

    # Mostrando información de las habitaciones antes de hacer las reservas
    print(habitacion1)
    print(habitacion2)

    # Realizando una reserva
    reserva1 = Reserva(huesped1, habitacion1, 3)  # 3 noches
    print(reserva1)

    # Haciendo la reserva en la habitación
    habitacion1.reservar()

    # Mostrando el estado de las habitaciones después de la reserva
    print(habitacion1)
    print(habitacion2)
