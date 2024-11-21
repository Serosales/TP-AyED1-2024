# Trabajo Práctico 8: Tuplas, conjuntos y diccionarios

""" Escribir un programa que permita ingresar un número entero N y genere un
diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la
tabla de multiplicar con el formato apropiado."""


def generar_tabla_multiplicar(numero: int) -> dict:
    """
    Genera la tabla de multiplicar de un número "numero" del 1 al 12 utilizando comprensión de diccionario.

    Pre:
    "numero" es un número entero.

    Post:
    Retorna un diccionario con las multiplicaciones de "numero" del 1 al 12.
    """
    return {multiplicador: numero * multiplicador for multiplicador in range(1, 13)}


def mostrar_tabla(tabla: dict, numero: int):
    """
    Muestra la tabla de multiplicar en un formato apropiado.

    Pre:
    "tabla" es un diccionario donde las claves son los multiplicadores (del 1 al 12)
    y los valores son los resultados de la multiplicación.
    "numero" es el número que se usó para generar la tabla.

    Post:
    Imprime la tabla de multiplicar en formato de tabla.
    """
    print(f"\nTabla de multiplicar de {numero}:")
    for multiplicador in range(1, 13):
        print(f"{numero} x {multiplicador} = {tabla[multiplicador]}")


def main() -> None:
    """
    Función principal que solicita al usuario un número y genera y muestra su tabla de multiplicar.

    Pre:
    El usuario ingresa un número entero.

    Post:
    Muestra la tabla de multiplicar en el formato apropiado.
    """
    # Solicitar al usuario el número
    try:
        numero_usuario = int(
            input("Ingrese un número entero para generar su tabla de multiplicar: ")
        )
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    # Generar la tabla de multiplicar
    tabla_multiplicacion = generar_tabla_multiplicar(numero_usuario)

    # Mostrar la tabla de multiplicar
    mostrar_tabla(tabla_multiplicacion, numero_usuario)


if __name__ == "__main__":
    main()
