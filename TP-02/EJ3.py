""" Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
donde N se ingresa desde el teclado.
 Luego se solicita imprimir los últimos 10 valores de la lista."""

# FUNCION: generar_cuadrados
def generar_cuadrados(N:int)-> int:
    """
    Genera una lista con los cuadrados de los números entre 1 y N (ambos incluidos).

    CONTRATO:
    PRE:
     N debe ser un entero positivo (N ≥ 1).

    POST:
        Retorna una lista de enteros.
        La lista contiene los cuadrados de los números desde 1 hasta N, ambos incluidos.
        La longitud de la lista es N.
        El valor en la posición i de la lista (donde i es un índice de 0 a N-1) es (i + 1) ** 2.
    """
    return list(map(lambda x: x**2, range(1, N + 1)))  # Usamos map y lambda para aplicar el cuadrado

# FUNCION:imprimir_ultimos_10_valores
def imprimir_ultimos_10_valores(lista: list) -> list:
    """
    Retorna los últimos 10 valores de la lista.

    CONTRATO:
    PRE:
        lista debe ser una lista de enteros.

    POST:
        Retorna una lista que contiene los últimos 10 valores de la lista proporcionada.
        Si la lista tiene menos de 10 elementos, se retornan todos los elementos de la lista.
    """
    ultimos_10 = lista[-10:] if len(lista) >= 10 else lista  # Obtener los últimos 10 o menos si no hay suficientes
    return ultimos_10


def main() -> None:
    """
    Solicita un valor entero al usuario, genera una lista de cuadrados de números hasta ese valor,
    y luego imprime los últimos 10 valores de la lista.

    CONTRATO:
    PRE:
        El usuario debe ingresar un entero positivo para N.

    POST:
        Imprime los últimos 10 valores de la lista de cuadrados de números desde 1 hasta N.
    """
    # Solicitar el valor de N
    N = int(input("Ingrese el valor de N: "))
    
    # Generar la lista con los cuadrados
    lista_cuadrados = generar_cuadrados(N)
    
    # Obtener e imprimir los últimos 10 valores de la lista
    ultimos_10_valores = imprimir_ultimos_10_valores(lista_cuadrados)
    print("Últimos 10 valores de la lista:", ultimos_10_valores)

if __name__ == "__main__":
    main()
