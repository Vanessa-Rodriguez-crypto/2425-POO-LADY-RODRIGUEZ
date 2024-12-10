# Clase que representa el clima semanal
# Contiene atributos y métodos relacionados con las temperaturas semanales.
class ClimaSemanal:
    def __init__(self):
        # Inicializa la lista de temperaturas y los días de la semana.
        self.temperaturas = []  # Lista para almacenar las temperaturas ingresadas
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    # Método para ingresar las temperaturas diarias
    # Solicita al usuario ingresar las temperaturas para cada día de la semana.
    def ingresar_temperaturas(self):
        print("Ingresa las temperaturas para cada día de la semana:")
        for dia in self.dias:
            temp = float(input(f"{dia}: "))  # Solicitar temperatura diaria
            self.temperaturas.append(temp)  # Agregar la temperatura a la lista

    # Método para calcular el promedio semanal
    # Devuelve el promedio de las temperaturas almacenadas.
    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)  # Suma las temperaturas y calcula el promedio

    # Método para mostrar el promedio semanal
    # Imprime el promedio calculado.
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()  # Calcular el promedio
        print(f"\nEl promedio semanal de la temperatura es: {promedio:.2f}°C")  # Mostrar resultado

# Programa principal
# Crea un objeto de la clase ClimaSemanal y coordina las operaciones.
if __name__ == "__main__":
    clima = ClimaSemanal()  # Crear instancia de la clase ClimaSemanal
    clima.ingresar_temperaturas()  # Llamar al método para ingresar temperaturas
    clima.mostrar_promedio()  # Llamar al método para mostrar el promedio
