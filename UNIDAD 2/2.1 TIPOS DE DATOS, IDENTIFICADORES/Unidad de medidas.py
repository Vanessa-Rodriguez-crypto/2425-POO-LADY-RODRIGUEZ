# Programa para convertir unidades de longitud (metros, centímetros, milímetros, kilómetros).
# Este programa solicita al usuario la longitud en una unidad de medida y la convierte a otras unidades.
# Se utilizan diferentes tipos de datos como integer, float, string, y boolean.

def convertir_longitud(valor, unidad_origen, unidad_destino):
    """
    Convierte una longitud desde una unidad de medida a otra.
    Parámetros:
    valor (float): La longitud a convertir.
    unidad_origen (string): La unidad de medida de entrada (metros, cm, mm, km).
    unidad_destino (string): La unidad de medida a la que convertir (metros, cm, mm, km).

    Retorna:
    float: El valor convertido en la unidad de destino.
    """

    # Diccionario que almacena los factores de conversión entre las unidades
    conversiones = {
        ('m', 'cm'): 100,  # 1 metro = 100 centímetros
        ('m', 'mm'): 1000,  # 1 metro = 1000 milímetros
        ('m', 'km'): 0.001,  # 1 metro = 0.001 kilómetros
        ('cm', 'm'): 0.01,  # 1 centímetro = 0.01 metros
        ('cm', 'mm'): 10,  # 1 centímetro = 10 milímetros
        ('cm', 'km'): 0.00001,  # 1 centímetro = 0.00001 kilómetros
        ('mm', 'm'): 0.001,  # 1 milímetro = 0.001 metros
        ('mm', 'cm'): 0.1,  # 1 milímetro = 0.1 centímetros
        ('mm', 'km'): 0.000001,  # 1 milímetro = 0.000001 kilómetros
        ('km', 'm'): 1000,  # 1 kilómetro = 1000 metros
        ('km', 'cm'): 100000,  # 1 kilómetro = 100000 centímetros
        ('km', 'mm'): 1000000  # 1 kilómetro = 1000000 milímetros
    }

    # Verificar si la conversión solicitada es válida
    if (unidad_origen, unidad_destino) not in conversiones:
        print("Error: La conversión solicitada no es válida.")
        return None

    # Obtener el factor de conversión y calcular el valor convertido
    factor_conversion = conversiones[(unidad_origen, unidad_destino)]
    valor_convertido = valor * factor_conversion
    return valor_convertido


def obtener_entrada_usuario():
    """
    Solicita al usuario la longitud y las unidades de origen y destino,
    y valida la entrada antes de realizar la conversión.
    """
    try:
        valor = float(input("Introduce la longitud a convertir: "))
        unidad_origen = input("Introduce la unidad de origen (m, cm, mm, km): ").lower()
        unidad_destino = input("Introduce la unidad de destino (m, cm, mm, km): ").lower()

        # Verificar si las unidades son válidas
        unidades_validas = ['m', 'cm', 'mm', 'km']
        if unidad_origen not in unidades_validas or unidad_destino not in unidades_validas:
            print("Error: Las unidades ingresadas no son válidas.")
            return

        # Llamar a la función de conversión y mostrar el resultado
        resultado = convertir_longitud(valor, unidad_origen, unidad_destino)

        if resultado is not None:
            print(f"{valor} {unidad_origen} son {resultado} {unidad_destino}.")

    except ValueError:
        print("Error: Por favor ingresa un valor numérico válido.")


# Ejecutar la función principal para solicitar datos al usuario y realizar la conversión
if __name__ == "__main__":
    obtener_entrada_usuario()
