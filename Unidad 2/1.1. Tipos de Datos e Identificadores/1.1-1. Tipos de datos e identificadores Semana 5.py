# Programa de conversión de unidades de temperatura
# Funcionalidad: Convierte unidades de temperatura entre Celsius, Fahrenheit y Kelvin.
# Tipos de Datos: Utiliza diferentes tipos de datos (float, str, bool) de manera adecuada.
# Identificadores: Utiliza identificadores descriptivos siguiendo la convención snake_case.

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    """
    Función que convierte unidades de temperatura.

    Parameters:
    - valor (float): Valor de la temperatura a convertir.
    - unidad_origen (str): Unidad de temperatura de origen (celsius, fahrenheit, kelvin).
    - unidad_destino (str): Unidad de temperatura de destino (celsius, fahrenheit, kelvin).

    Returns:
    - float: Valor de la temperatura convertida.
    """
    # Validar unidades
    unidades_validas = ['celsius', 'fahrenheit', 'kelvin']
    if unidad_origen.lower() not in unidades_validas or unidad_destino.lower() not in unidades_validas:
        print("Unidad de temperatura no válida.")
        return None

    # Realizar la conversión
    if unidad_origen.lower() == 'celsius':
        if unidad_destino.lower() == 'fahrenheit':
            resultado = (valor * 9/5) + 32
        elif unidad_destino.lower() == 'kelvin':
            resultado = valor + 273.15
        else:
            resultado = valor  # Si la unidad destino es Celsius, no es necesario convertir
    elif unidad_origen.lower() == 'fahrenheit':
        if unidad_destino.lower() == 'celsius':
            resultado = (valor - 32) * 5/9
        elif unidad_destino.lower() == 'kelvin':
            resultado = (valor - 32) * 5/9 + 273.15
        else:
            resultado = valor  # Si la unidad destino es Fahrenheit, no es necesario convertir
    else:  # Unidad origen es Kelvin
        if unidad_destino.lower() == 'celsius':
            resultado = valor - 273.15
        elif unidad_destino.lower() == 'fahrenheit':
            resultado = (valor - 273.15) * 9/5 + 32
        else:
            resultado = valor  # Si la unidad destino es Kelvin, no es necesario convertir

    return resultado

# Ejemplo de uso del programa
temperatura = 25.0
unidad_origen = 'celsius'
unidad_destino = 'fahrenheit'

# Llamada a la función de conversión
resultado = convertir_temperatura(temperatura, unidad_origen, unidad_destino)

# Imprimir el resultado si la conversión fue exitosa
if resultado is not None:
    print(f"{temperatura} grados {unidad_origen} es igual a {resultado:.2f} grados {unidad_destino}")

