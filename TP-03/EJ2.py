""" Las siguientes matrices responden distintos patrones de relleno. Desarrollar funciones que generen cada una de ellas sin intervención humana y escribir un programa
que las invoque e imprima por pantalla. El tamaño de las matrices debe establecerse como N x N, donde N se ingresa a través del teclado."""

from typing import List


# FUNCIÓN: matriz_a
def matriz_a(N: int) -> List[List[int]]:
    """Genera una matriz N x N con el patrón de la matriz A.

    CONTRATO:
    PRE:
        N es un entero mayor o igual a 0.
    POST:
        Retorna una matriz N x N con un 1 en la posición (0,0) si N > 0, y 0 en el resto de posiciones.
    """
    matriz = [[0] * N for _ in range(N)]
    if N > 0:
        matriz[0][0] = 1
    return matriz


# FUNCIÓN: matriz_b
def matriz_b(N: int) -> List[List[int]]:
    """Genera una matriz N x N con el patrón de la matriz B.

    CONTRATO:
    PRE:
        N es un entero mayor o igual a 0.
    POST:
        Retorna una matriz N x N con un 27 en la posición (N-1,N-1) si N > 0, y 0 en el resto de posiciones.
    """
    matriz = [[0] * N for _ in range(N)]
    if N > 0:
        matriz[N - 1][N - 1] = 27
    return matriz


# FUNCIÓN: matriz_c
def matriz_c(N: int) -> List[List[int]]:
    """Genera una matriz N x N con el patrón de la matriz C.
    CONTRATO:
    PRE: N es un entero mayor o igual a 0.
    POST: Retorna una matriz N x N con valores decrecientes en la primera columna desde 4 hasta 0 si i < 4, y 0 en la posición (3,0).
    """
    matriz = [[0] * N for _ in range(N)]
    for i in range(min(N, 4)):
        matriz[i][0] = 4 - i
    return matriz


# FUNCIÓN: matriz_d
def matriz_d(N: int) -> List[List[int]]:
    """Genera una matriz N x N con el patrón de la matriz D.

    CONTRATO:
    PRE:
        N es un entero mayor o igual a 0.
    POST:
        Retorna una matriz N x N con todos los elementos igual a 8.
    """
    return [[8] * N for _ in range(N)]


# FUNCIÓN: matriz_e
def matriz_e(N: int) -> List[List[int]]:
    """Genera una matriz N x N con el patrón de la matriz E.

    CONTRATO:
    PRE:
        N es un entero mayor o igual a 0.
    POST:
        Retorna una matriz N x N con valores en la diagonal principal que son (i + 1) % 4.
    """
    return [[(i + 1) % 4 if i == j else 0 for j in range(N)] for i in range(N)]


# FUNCIÓN: matriz_f
def matriz_f(N: int) -> List[List[int]]:
    """Genera una matriz N x N con el patrón de la matriz F.

    CONTRATO:
    PRE:
        N es un entero mayor o igual a 0.
    POST:
        Retorna una matriz N x N con valores 1 en las posiciones donde la suma de los índices es impar.
    """
    return [[1 if (i + j) % 2 == 1 else 0 for j in range(N)] for i in range(N)]


# FUNCIÓN: matriz_g
def matriz_g(N: int) -> List[List[int]]:
    """Genera una matriz N x N con el patrón de la matriz G.

    CONTRATO:
    PRE:
        N es un entero mayor o igual a 0.
    POST:
        Retorna una matriz N x N con valores que son la suma de los índices (i + j + 1).
    """
    return [[i + j + 1 for j in range(N)] for i in range(N)]


# FUNCIÓN: matriz_h
def matriz_h(N: int) -> List[List[int]]:
    """Genera una matriz N x N con el patrón de la matriz H.

    CONTRATO:
    PRE:
         N es un entero mayor o igual a 0.
    POST:
        Retorna una matriz N x N con valores i + j + 1 si N > 1.
    """
    return [[i + j + 1 if N > 1 else 0 for j in range(N)] for i in range(N)]


# FUNCIÓN: matriz_i
def matriz_i(N: int) -> List[List[int]]:
    """Genera una matriz N x N con el patrón de la matriz I.

    CONTRATO:
    PRE:
        N es un entero mayor o igual a 0.
    POST:
    Retorna una matriz N x N con valores (i + 1) * (j + 1) en las posiciones donde i + j < N.
    """
    return [[(i + 1) * (j + 1) if i + j < N else 0 for j in range(N)] for i in range(N)]


# FUNCIÓN: imprimir_matriz
def imprimir_matriz(matriz: List[List[int]]) -> None:
    """Imprime la matriz de forma legible.

    PRE:
        matriz es una lista de listas de enteros.
    POST:
        Imprime la matriz en formato de tabla.
    """
    for fila in matriz:
        print(" ".join(map(str, fila)))


def main() -> None:
    """Función principal que solicita el tamaño de la matriz y muestra todas las matrices generadas.

    CONTRATO:
    PRE: 
        Se solicita al usuario ingresar un valor entero para el tamaño de la matriz.
    POST: 
        Imprime las matrices generadas con los diferentes patrones.
    """
    N = int(input("Ingrese el valor de N (tamaño de la matriz N x N): "))

    print("\nMatriz A:")
    imprimir_matriz(matriz_a(N))

    print("\nMatriz B:")
    imprimir_matriz(matriz_b(N))

    print("\nMatriz C:")
    imprimir_matriz(matriz_c(N))

    print("\nMatriz D:")
    imprimir_matriz(matriz_d(N))

    print("\nMatriz E:")
    imprimir_matriz(matriz_e(N))

    print("\nMatriz F:")
    imprimir_matriz(matriz_f(N))

    print("\nMatriz G:")
    imprimir_matriz(matriz_g(N))

    print("\nMatriz H:")
    imprimir_matriz(matriz_h(N))

    print("\nMatriz I:")
    imprimir_matriz(matriz_i(N))


if __name__ == "__main__":
    main()
