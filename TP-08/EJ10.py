# Trabajo Práctico 8: Tuplas, conjuntos y diccionarios

""" . Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario
y una lista de claves. La función debe eliminar del diccionario todas las claves
contenidas en la lista, devolviendo el diccionario modificado y un número entero
que represente la cantidad de claves eliminadas. Desarrollar también un programa
para verificar su comportamiento.
"""


def eliminar_claves(diccionario: dict, claves: list) -> tuple:
    """
    Elimina las claves especificadas de un diccionario, con manejo de errores.

    Pre:
    diccionario: Un diccionario del cual se eliminarán las claves.
    claves: Una lista de claves que se desean eliminar del diccionario.

    Post:
    Retorna el diccionario modificado y una lista de valores booleanos indicando si cada clave fue eliminada o no.
    """
    resultados_eliminacion = []

    for clave in claves:
        if clave in diccionario:
            diccionario.pop(clave)
            resultados_eliminacion.append(True)
        else:
            resultados_eliminacion.append(False)

    return diccionario, resultados_eliminacion


def main() -> None:
    """
    Programa principal que solicita un diccionario y una lista de claves a eliminar.
    Verifica el comportamiento de la función eliminar_claves.

    Pre:
    No es necesario que el diccionario o las claves sean proporcionadas por el usuario; están predefinidos.
    La lista de claves debe ser proporcionada con valores que pueden o no estar en el diccionario original.

    Post:
    El programa imprimirá el diccionario original y el diccionario modificado después de las eliminaciones.
    Informará sobre el estado de eliminación de cada clave: si se eliminó con éxito o no.
    """
    # Ejeplo de diccionario
    diccionario_inicial = {
        1: 1,
        2: 4,
        3: 9,
        4: 16,
        5: 25,
        6: 36,
        7: 49,
        8: 64,
        9: 81,
        10: 100,
        11: 121,
        12: 144,
        13: 169,
        14: 196,
        15: 225,
        16: 256,
        17: 289,
        18: 324,
        19: 361,
        20: 400,
    }

    print("Diccionario original:", diccionario_inicial)

    # Lista de claves a eliminar (algunas claves no están en el diccionario)
    claves_a_eliminar = [1, 5, 22, 34, 9, 11, 5, 19]

    # Llamamos a la función eliminar_claves
    diccionario_modificado, resultados = eliminar_claves(
        diccionario_inicial.copy(), claves_a_eliminar
    )

    # Imprimimos el diccionario modificado
    print("Diccionario modificado:", diccionario_modificado)

    # Informamos sobre el estado de eliminación de cada clave
    for clave, resultado in zip(claves_a_eliminar, resultados):
        estado = "fue eliminada con éxito" if resultado else "no se pudo eliminar"
        print(f"La clave {clave} {estado}")


if __name__ == "__main__":
    main()
