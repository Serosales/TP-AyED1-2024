# Trabajo Práctico 8: Tuplas, conjuntos y diccionarios

""" Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y
 20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves."""


def generar_diccionario_cuadrados() -> dict:
    """
    Genera un diccionario donde las claves son números enteros del 1 al 20
    y los valores son el cuadrado de las claves.

    Post:
    Retorna un diccionario con las claves y sus cuadrados.
    """
    return {numero: numero**2 for numero in range(1, 21)}


def imprimir_diccionario(diccionario: dict):
    """
    Imprime el diccionario en un formato legible.

    Pre:
    "diccionario" es un diccionario donde las claves son números enteros
    y los valores son sus cuadrados.

    Post:
    Imprime el diccionario en formato clave: valor.
    """
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")


def main() -> None:
    """
    Función principal que genera e imprime el diccionario de cuadrados.
    """
    # Generar el diccionario de cuadrados
    diccionario_cuadrados = generar_diccionario_cuadrados()

    # Imprimir el diccionario
    imprimir_diccionario(diccionario_cuadrados)


if __name__ == "__main__":
    main()
