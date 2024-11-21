# Trabajo Práctico 8: Tuplas, conjuntos y diccionarios

""" Escribir una función buscarclave() que reciba como parámetros un diccionario y un
valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el diccionario. Comprobar el comportamiento de la función mediante un programa apropiado. """


def buscar_clave(diccionario: dict, valor: any) -> list:
    """
    Busca todas las claves en el diccionario que mapeen al valor dado.

    Pre:
    diccionario: Diccionario con claves de cualquier tipo y valores de cualquier tipo.
    valor: Un valor de cualquier tipo que se busca en el diccionario.
    El valor debe ser del mismo tipo que los valores almacenados en el diccionario.

    Post:
    Devuelve una lista de claves que tienen asociado el valor buscado.
    Si no se encuentra el valor, la lista será vacía.

    """
    claves = []
    for clave, valor_actual in diccionario.items():
        if valor_actual == valor:
            claves.append(clave)
    return claves


def main() -> None:
    """
    Función principal para ejecutar ejemplos de uso de la función buscar_clave.

    Pre:
     Se espera que el diccionario `lista_precios` esté definido con claves de tipo (str)
    y valores de tipo (int). El valor de búsqueda debe ser un entero que sea uno de los valores
    presentes en el diccionario.

    Post:
    La función "buscar_clave" se llama para buscar las claves asociadas a los valores especificados
    en el diccionario y se imprime el resultado. Si no se encuentra el valor, se imprimirá una lista vacía.

    """

    lista_precios = {
        "lapicera": 100,
        "borrador": 45,
        "tiza": 45,
        "fibrón": 75,
        "lápiz": 120,
        "resaltador": 80,
        "regla": 120,
    }

    # Buscar claves asociadas al precio 45
    resultado = buscar_clave(lista_precios, 45)

    # Buscar claves asociadas al precio 120
    resultado2 = buscar_clave(lista_precios, 120)

    # Imprimir los resultados
    print(f"Las claves que mapean al valor 45 son: {resultado}")
    print(f"Las claves que mapean al valor 120 son: {resultado2}")


if __name__ == "__main__":
    main()
