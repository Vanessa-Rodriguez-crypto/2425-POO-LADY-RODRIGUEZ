class Archivo:
    """
    Clase que representa un archivo y gestiona su apertura, escritura y cierre.
    """

    def __init__(self, nombre_archivo, modo):
        """
        Constructor: Inicializa los atributos del objeto y abre el archivo.

        :param nombre_archivo: Nombre del archivo que se gestionará.
        :param modo: Modo en el que se abrirá el archivo (e.g., 'w', 'r', 'a').
        """
        self.nombre_archivo = nombre_archivo
        self.modo = modo

        # Abre el archivo al crear el objeto.
        try:
            self.archivo = open(nombre_archivo, modo)
            print(f"Archivo '{nombre_archivo}' abierto en modo '{modo}'.")
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")
            self.archivo = None

    def escribir(self, texto):
        """
        Escribe texto en el archivo abierto. Verifica que el archivo esté abierto.

        :param texto: El contenido a escribir en el archivo.
        """
        if self.archivo and not self.archivo.closed:
            self.archivo.write(texto)
            print(f"Texto escrito en el archivo '{self.nombre_archivo}'.")
        else:
            print("No se puede escribir: el archivo está cerrado o no fue abierto correctamente.")

    def __del__(self):
        """
        Destructor: Cierra el archivo si está abierto y limpia los recursos.
        """
        if self.archivo and not self.archivo.closed:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado automáticamente al eliminar el objeto.")
        else:
            print(f"Archivo '{self.nombre_archivo}' ya estaba cerrado o no fue abierto correctamente.")


# Ejemplo de uso:
if __name__ == "__main__":
    # Crear un objeto de la clase Archivo
    archivo = Archivo("codigo.txt", "w")

    # Escribir en el archivo
    archivo.escribir("Hola, este es un ejemplo de uso de constructores y destructores en Python.\n")
    archivo.escribir("Este texto será escrito en el archivo codigo.txt.\n")

    # Eliminar manualmente el objeto (invoca el destructor)
    del archivo

    print("Fin del programa. Si el destructor no se invocó antes, se invocará automáticamente ahora.")
