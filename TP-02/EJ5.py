""" Escribir una función que reciba una lista como parámetro y devuelva True si la lista
está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
además un programa para verificar el comportamiento de la función. """


# FUNCION:ordenada
def ordenada(lst):
    """
    Verifica si la lista está ordenada en forma ascendente.

    CONTRATO:
    PRE:
     lst: debe ser una lista de elementos comparables (del mismo tipo o tipos que se pueden comparar).

    POST:
     Retorna True si la lista está ordenada en forma ascendente, False en caso contrario.
     Compara la lista original con la lista ordenada (convertida a cadenas si es necesario). Si son iguales, la lista está ordenada.
    """
    # Compara la lista original con su versión ordenada
    return lst == list(map(str, sorted(lst)))


# FUNCION:verificar_ordenada
def verificar_ordenada():
    """
    Verifica el comportamiento de la función ordenada con varias listas de prueba.

    CONTRATO:
    PRE:
     No hay datos de entrada. La función define internamente las listas de prueba.
     Las listas de prueba deben ser listas de elementos comparables entre sí.

    POST:
    - Imprime si cada lista de prueba está ordenada (True) o no (False).
    """
    listas = [
        [1, 2, 3],  # Ordenada
        ["a", "b", "c"],  # Ordenada
        [3, 2, 1],  # No ordenada
        ["b", "a"],  # No ordenada
        [1, 1, 1],  # Ordenada
        [],  # Ordenada (lista vacía)
    ]

    for lst in listas:
        resultado = ordenada(lst)
        print(f"La lista {lst} está ordenada: {resultado}")

# FUNCION: main
def main():
    """
    Función principal que ejecuta la verificación de las listas.

    CONTRATO:
    PRE:
     No recibe datos de entrada.

    POST:
     Llama a verificar_ordenada para imprimir los resultados de la verificación.
    """
    verificar_ordenada()


if __name__ == "__main__":
    main()
