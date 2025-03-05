class Libro:
    """
    Representa un libro con atributos inmutables de título y autor (almacenados en una tupla),
    además de categoría e ISBN.
    """
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Tupla inmutable para título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo_autor[0]} de {self.titulo_autor[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    """
    Representa un usuario de la biblioteca con un nombre, un ID único y una lista de libros prestados.
    """
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    """
    Gestiona los libros disponibles, los usuarios registrados y el historial de préstamos.
    """
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave para acceso eficiente
        self.usuarios_registrados = set()  # Conjunto para IDs únicos de usuarios
        self.historial_prestamos = {}  # Diccionario para registrar préstamos por usuario

    def agregar_libro(self, libro):
        """Añade un libro a la biblioteca si el ISBN no está ya registrado."""
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("El libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        """Elimina un libro de la biblioteca por su ISBN."""
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            print(f"Libro eliminado: {libro}")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        """Registra un nuevo usuario en la biblioteca si su ID no está registrado."""
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.historial_prestamos[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("El usuario ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        """Elimina a un usuario de la biblioteca si está registrado."""
        if id_usuario in self.usuarios_registrados:
            usuario = self.historial_prestamos.pop(id_usuario)
            self.usuarios_registrados.remove(id_usuario)
            print(f"Usuario eliminado: {usuario}")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, id_usuario, isbn):
        """Presta un libro a un usuario si ambos existen y el libro está disponible."""
        if id_usuario in self.usuarios_registrados and isbn in self.libros_disponibles:
            usuario = self.historial_prestamos[id_usuario]
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro prestado: {libro} a {usuario.nombre}")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        """Permite a un usuario devolver un libro a la biblioteca."""
        if id_usuario in self.usuarios_registrados:
            usuario = self.historial_prestamos[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Libro devuelto: {libro} por {usuario.nombre}")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        """Busca libros en la biblioteca según un criterio específico (título, autor o categoría)."""
        encontrados = [libro for libro in self.libros_disponibles.values() if getattr(libro, criterio) == valor]
        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados(self, id_usuario):
        """Lista los libros prestados a un usuario específico."""
        if id_usuario in self.usuarios_registrados:
            usuario = self.historial_prestamos[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# Pruebas del sistema
biblioteca = Biblioteca()

# Agregar libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "78945")
libro2 = Libro("1984", "George Orwell", "Ficción", "67890")
libro3 = Libro("El principito", "Antoine de Saint-Exupéry", "Fábula", "18964")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Registrar usuarios
usuario1 = Usuario("Fernando Mejia", "U001")
usuario2 = Usuario("Laura Rodriguez", "U002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("U001", "78945")

# Listar libros prestados
biblioteca.listar_libros_prestados("U001")

# Devolver libro
biblioteca.devolver_libro("U001", "78945")

# Buscar libro
biblioteca.buscar_libro("categoria", "Ficción")
