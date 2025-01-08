# Clase que representa un Libro
class Libro:
    def __init__(self, titulo, autor, isbn):
        """
        Inicializa un libro con su título, autor e ISBN.
        """
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True  # Inicialmente el libro está disponible

    def prestar(self):
        """
        Marca el libro como prestado.
        """
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible para préstamo.")

    def devolver(self):
        """
        Marca el libro como devuelto y disponible nuevamente.
        """
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto y está disponible.")

    def __str__(self):
        """
        Retorna una representación en cadena del libro.
        """
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo}' de {self.autor} (ISBN: {self.isbn}) - Estado: {estado}"


# Clase que representa a un Miembro
class Miembro:
    def __init__(self, nombre, miembro_id):
        """
        Inicializa un miembro con su nombre y número de identificación.
        """
        self.nombre = nombre
        self.miembro_id = miembro_id

    def __str__(self):
        """
        Retorna una representación en cadena del miembro.
        """
        return f"Miembro: {self.nombre} (ID: {self.miembro_id})"


# Clase que representa el Sistema de Préstamos
class SistemaPrestamos:
    def __init__(self):
        """
        Inicializa el sistema de préstamos con una lista vacía de libros y miembros.
        """
        self.libros = []
        self.miembros = []

    def agregar_libro(self, libro):
        """
        Agrega un libro al sistema.
        """
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado al sistema.")

    def registrar_miembro(self, miembro):
        """
        Registra un miembro en el sistema.
        """
        self.miembros.append(miembro)
        print(f"Miembro '{miembro.nombre}' registrado en el sistema.")

    def prestar_libro(self, libro, miembro):
        """
        Realiza el préstamo de un libro a un miembro si está disponible.
        """
        if libro in self.libros and miembro in self.miembros:
            if libro.disponible:
                libro.prestar()
            else:
                print(f"El libro '{libro.titulo}' no está disponible para préstamo.")
        else:
            print("El libro o el miembro no están registrados en el sistema.")

    def devolver_libro(self, libro):
        """
        Realiza la devolución de un libro.
        """
        if libro in self.libros:
            libro.devolver()
        else:
            print("El libro no está registrado en el sistema.")

    def mostrar_libros(self):
        """
        Muestra todos los libros del sistema.
        """
        for libro in self.libros:
            print(libro)


# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancias de los objetos
    libro1 = Libro("1984", "George Orwell", "123456789")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "987654321")
    miembro1 = Miembro("Pedro Escobar", "001")
    miembro2 = Miembro("Ana Lucia Perez", "002")

    # Crear el sistema de préstamos
    sistema = SistemaPrestamos()

    # Agregar libros y registrar miembros al sistema
    sistema.agregar_libro(libro1)
    sistema.agregar_libro(libro2)
    sistema.registrar_miembro(miembro1)
    sistema.registrar_miembro(miembro2)

    # Mostrar los libros disponibles
    print("\nLibros disponibles en la biblioteca:")
    sistema.mostrar_libros()

    # Realizar un préstamo
    sistema.prestar_libro(libro1, miembro1)

    # Intentar prestar un libro que ya está prestado
    sistema.prestar_libro(libro1, miembro2)

    # Devolver un libro
    sistema.devolver_libro(libro1)

    # Mostrar el estado final de los libros
    print("\nEstado final de los libros:")
    sistema.mostrar_libros()
