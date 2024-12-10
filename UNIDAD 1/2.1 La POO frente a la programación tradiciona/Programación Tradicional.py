# Función para ingresar temperaturas diarias
# Esta función solicita al usuario ingresar las temperaturas para cada día de la semana
# y almacena estas temperaturas en una lista.
def ingresar_temperaturas():
    temperaturas = []  # Lista para almacenar las temperaturas ingresadas
    print("Ingresa las temperaturas para cada día de la semana:")
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for dia in dias:
        temp = float(input(f"{dia}: "))  # Solicitar temperatura diaria
        temperaturas.append(temp)  # Agregar la temperatura a la lista
    return temperaturas

# Función para calcular el promedio semanal
# Toma una lista de temperaturas como entrada y devuelve el promedio.
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)  # Suma las temperaturas y las divide por su cantidad

# Programa principal
# Coordina las funciones para ingresar temperaturas y calcular el promedio semanal.
def main():
    temperaturas = ingresar_temperaturas()  # Obtener las temperaturas
    promedio = calcular_promedio(temperaturas)  # Calcular el promedio
    print(f"\nEl promedio semanal de la temperatura es: {promedio:.2f}°C")  # Mostrar resultado

# Punto de entrada del programa
if __name__ == "__main__":
    main()
