# Trabajo Práctico 8: Tuplas, conjuntos y diccionarios

""". Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
o False. Escribir también un programa para verificar su comportamiento. Considerar
el uso de conjuntos para resolver este ejercicio. """


def fichas_encajan(ficha_1: tuple, ficha_2: tuple) -> bool:
    """
    Determina si dos fichas de dominó encajan (tienen al menos un número en común).

    Pre:
    ficha_1 y ficha_2 son tuplas con dos elementos enteros (x, y), que representan las fichas de dominó.

    Post:
    Retorna True si las fichas encajan (tienen al menos un número en común), False en caso contrario.
    """
    # Comparar directamente los elementos de las dos fichas
    comparar = (
        ficha_1[0] == ficha_2[0]
        or ficha_1[0] == ficha_2[1]
        or ficha_1[1] == ficha_2[0]
        or ficha_1[1] == ficha_2[1]
    )
    return comparar


def obtener_ficha(numero: int) -> tuple:
    """
    Solicita al usuario que ingrese los números de una ficha de dominó.

    Pre:
    numero es un entero que indica el número de la ficha que se está solicitando (1 o 2).

    Post:
    Retorna una tupla con los dos números de la ficha ingresada por el usuario.
    """
    while True:
        try:
            f_1 = int(input(f"Ingrese el primer número de la ficha {numero}: "))
            f_2 = int(input(f"Ingrese el segundo número de la ficha {numero}: "))
            return (f_1, f_2)
        except ValueError:
            print("Por favor, ingrese números enteros válidos.")


def main() -> None:
    """
    Función principal que permite al usuario ingresar dos fichas de dominó y verifica si encajan.

    Pre:
    El usuario debe ingresar dos números enteros para cada ficha de dominó.

    Post:
    Imprime un mensaje indicando si las fichas encajan o no.
    No retorna ningún valor.
    """
    # Obtener las fichas del usuario
    ficha_1 = obtener_ficha(1)
    ficha_2 = obtener_ficha(2)

    # Verificar si las fichas encajan y mostrar el resultado
    if fichas_encajan(ficha_1, ficha_2):
        print(f"Las fichas {ficha_1} y {ficha_2} encajan.")
    else:
        print(f"Las fichas {ficha_1} y {ficha_2} no encajan.")


if __name__ == "__main__":
    main()
