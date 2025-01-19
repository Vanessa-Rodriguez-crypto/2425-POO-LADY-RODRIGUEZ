# Clase base: Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        # Atributos encapsulados
        self._marca = marca  # Uso de un guion bajo para indicar encapsulación
        self._modelo = modelo

    # Método público para obtener información del vehículo
    def obtener_informacion(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}"

    # Método que puede ser sobrescrito (polimorfismo)
    def tipo_vehiculo(self):
        return "Vehículo genérico"

# Clase derivada: Auto
class Auto(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base
        self._num_puertas = num_puertas

    # Sobrescritura del método para mostrar polimorfismo
    def tipo_vehiculo(self):
        return "Auto"

    # Método específico de la clase Auto
    def obtener_informacion(self):
        info_base = super().obtener_informacion()
        return f"{info_base}, Número de puertas: {self._num_puertas}"

# Clase derivada: Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo_moto):
        super().__init__(marca, modelo)
        self._tipo_moto = tipo_moto

    # Sobrescritura del método para mostrar polimorfismo
    def tipo_vehiculo(self):
        return "Moto"

    # Método específico de la clase Moto
    def obtener_informacion(self):
        info_base = super().obtener_informacion()
        return f"{info_base}, Tipo de moto: {self._tipo_moto}"

# Programa principal para demostrar la funcionalidad
def main():
    # Creación de instancias
    vehiculo_generico = Vehiculo("Genérico", "Modelo X")
    auto = Auto("Toyota", "Corolla", 4)
    moto = Moto("Yamaha", "R3", "Deportiva")

    # Uso de métodos
    print("--- Información de los Vehículos ---")
    print(vehiculo_generico.obtener_informacion())
    print(auto.obtener_informacion())
    print(moto.obtener_informacion())

    print("\n--- Tipos de Vehículos (Polimorfismo) ---")
    for vehiculo in [vehiculo_generico, auto, moto]:
        print(f"{vehiculo.obtener_informacion()} - Tipo: {vehiculo.tipo_vehiculo()}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
