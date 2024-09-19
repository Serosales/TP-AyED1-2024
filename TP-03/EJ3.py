""" Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N2
), de tal forma que ningún número se repita. Imprimir la matriz por pantalla."""

import random as rn
from typing import List


# FUNCIÓN:generar_matriz_unica(
def generar_matriz_unica(N: int) -> List[List[int]]:
    """
    CONTRATO:
    PRE:
        N > 0.
    POST:
        Retorna una matriz N x N con números enteros únicos en el intervalo [0, N^2).
    """
    max_num = N * N
    numeros = rn.sample(
        range(max_num), max_num
    )  # Genera una lista de números únicos aleatorios

    # Crear la matriz usando comprensión de listas
    matriz = [numeros[i * N : (i + 1) * N] for i in range(N)]

    return matriz


# FUNCIÓN:
def imprimir_matriz(matriz: List[List[int]]) -> None:
    """
    CONTRATO:
    PRE:
        matriz es una lista de listas de enteros.
    POST:
        Imprime la matriz de forma legible en la consola.
    """
    print("\n".join(" ".join(map(str, fila)) for fila in matriz))


# FUNCIÓN: main
def main() -> None:
    """
    CONTRATO:
    PRE:
        El valor de N se ingresa correctamente como un entero.
    POST:
        Imprime la matriz N x N generada con números únicos y aleatorios,
        si N es mayor que 0. Si N <= 0, se imprime un mensaje de error.

    """

    N = int(input("Ingrese el valor de N (tamaño de la matriz N x N): "))

    if N <= 0:
        print("El tamaño de la matriz debe ser mayor que 0.")
        return

    matriz = generar_matriz_unica(N)

    print("\nMatriz generada:")
    imprimir_matriz(matriz)


if __name__ == "__main__":
    main()
