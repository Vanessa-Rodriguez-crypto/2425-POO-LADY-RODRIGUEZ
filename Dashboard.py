import os
def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {os.path.basename(ruta_script)} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(os.path.abspath(__file__))

    opciones = {
        '1' : os.path.join("UNIDAD 1", "1.2 TECNICA DE PROGRAMACION", "TECNICA DE PROGRAMACION.py"),
        '2' : os.path.join("UNIDAD 1", "2.1 La POO frente a la programación tradiciona",
                          "Programación Orientada a Objetos (POO).py"),
        '3' : os.path.join("UNIDAD 1", "2.1 La POO frente a la programación tradiciona", "Programación Tradicional.py"),
        '4' : os.path.join("UNIDAD 1", "2.2 CARACTERISTICAS DE LA PROGRAMACION ORIENTADA A OBJECTO", "MundoReal_POO",
                          "Biblioteca.py"),
        '5' : os.path.join("UNIDAD 1", "2.2 CARACTERISTICAS DE LA PROGRAMACION ORIENTADA A OBJECTO", "MundoReal_POO",
                          "Reserva de un Hotel.py"),
        '6' : os.path.join("UNIDAD 1", "2.2 CARACTERISTICAS DE LA PROGRAMACION ORIENTADA A OBJECTO", "MundoReal_POO",
                          "Tienda de dos clientes.py"),
        '7' : os.path.join("UNIDAD 2", "2.1 TIPOS DE DATOS, IDENTIFICADORES", "Unidad de medidas.py"),
        '8' : os.path.join("UNIDAD 2", "T1.2 Objetos, clases, Herencia, Encapsulamiento, Polimorfismo", "COCHES.py"),
        '9' : os.path.join("UNIDAD 2", "T1.3 CONSTRUCTORES Y DESTRUCTORES", "GESTIÓN DE ARCHIVOS.py"),
    }

    while True:
        print("\n******** Menu Principal - Dashboard *************")
        for key, value in opciones.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
