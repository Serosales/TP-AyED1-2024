"""Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los
elementos de la primera que sean impares. El proceso deberá realizarse utilizando
la función filter(). Imprimir las dos listas por pantalla.  """

from  random  import randint as rn
from typing import List

# FUNCIÓN: generar_lista
def generar_lista()->list[int]:
    """
    CONTRATO:
    PRE:
        Ninguna
    POST:
        Retorna una lista de 20 números aleatorios entre 1 y 100"""
    return [rn(1, 100) for _ in range(20)]

# FUNCIÓN: filtrar_impares
def filtrar_impares(lista:list[int])->list[int]:

    """
    CONTRATO:
    PRE: 
        lista (una lista de enteros)
     POST: 
        Retorna una lista con los elementos impares de la lista de entrada
    """
    return list(filter(lambda x: x % 2 != 0, lista))

# FUNCIÓN main
def main()->None:
    """
    CONTRATO:
    PRE: 
        Ninguna

    POST: 
        Imprime la lista original y la lista de números impares.
        No tiene parametros de retorno."""
    # Generar una lista con números al azar entre 1 y 100
    lista_original = generar_lista()

    # Crear una nueva lista con los elementos impares usando filter()
    lista_impares = filtrar_impares(lista_original)

    # Imprimir las dos listas
    print(f"Lista original: {lista_original}")
    print(f"Lista con números impares: {lista_impares}")



if __name__ == "__main__":
    main()
