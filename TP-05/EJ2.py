# Trabajo Práctico 5: Manejo de excepciones

""" . Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, sume ambos valores y devuelva el resultado como un
número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error."""
# FUNCIÓN: Sumar dos números reales representados como cadenas
def sumar_reales(cadena_a: str, cadena_b: str) -> float:
    """
    Suma dos números reales representados como cadenas.

    PRE:
        cadena_1 (str): Contiene un número real.
        cadena_2 (str): Contiene un número real.

    POST:
        Retorna la suma de los dos números si ambas cadenas son válidas.
        Si alguna de las cadenas no contiene un número válido, retorna -1.
    """
    try:
        # Intentar convertir las cadenas a números flotantes
        numero_1 = float(cadena_a)
        numero_2 = float(cadena_b)
        # Retornar la suma de ambos números
        return numero_1 + numero_2
    except ValueError:
        # Devolver -1 si hay un error en la conversión
        return -1


# FUNCIÓN: Programa principal para gestionar la interacción con el usuario
def ejecutar_suma() -> None:
    """
    Función principal que gestiona el flujo del programa interactivo.

    PRE:
        No requiere parámetros. El usuario ingresa dos cadenas de números reales a través de la entrada estándar.

    POST:
        Solicita al usuario que ingrese dos cadenas representando números reales.
        Si las cadenas contienen números válidos, muestra la suma de los números en formato con dos decimales.
        Si alguna de las cadenas no es válida, muestra un mensaje de error.
        Permite al usuario salir del programa escribiendo 'salir'.
    """
    while True:
        cadena_1 = input(
            "Ingrese la primera cadena ( 'salir' para terminar el programa. ): "
        )
        if cadena_1.lower() == "salir":
            print("Saliendo del programa.")
            break

        cadena_2 = input(
            "Ingrese la segunda cadena ( 'salir' para terminar el programa. ): "
        )
        if cadena_2.lower() == "salir":
            print("Saliendo del programa.")
            break

        # Llamar a la función sumar_reales para obtener el resultado
        resultado = sumar_reales(cadena_1, cadena_2)

        # Verificar si la suma fue válida o hubo un error
        if resultado == -1:
            print("Error: Contiene un número no válido.")
        else:
            print(f"La suma de los números es: {resultado:.2f}")  


if __name__ == "__main__":
    ejecutar_suma()