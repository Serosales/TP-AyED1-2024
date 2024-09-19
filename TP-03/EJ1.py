""" 1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada función:
a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
teclado.
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
parámetro.
g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
una lista con los números de las mismas.
NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera
sea el valor ingresado."""

from typing import List, Tuple

# FUNCIÓN: Cargar números enteros en una matriz de N x N desde el teclado.
def cargar_matriz(N: int) -> List[List[int]]:
    """
    PRE: 
        N es un entero positivo.
    POST: 
        Retorna una matriz de tamaño N x N cargada con números enteros ingresados desde el teclado.
    """
    matriz = []
    for i in range(N):
        fila = list(map(int, input(f"Ingrese los elementos de la fila {i + 1} (separados por espacios): ").split()))
        if len(fila) != N:
            print(f"Advertencia: La cantidad de elementos en la fila {i + 1} no coincide con N. Se llenará la fila con ceros.")
            fila += [0] * (N - len(fila))  # Completa la fila con ceros si hay menos elementos
        matriz.append(fila)
    return matriz

# FUNCIÓN: Ordenar en forma ascendente cada una de las filas de la matriz.
def ordenar_filas(matriz: List[List[int]]) -> List[List[int]]:
    """PRE:
      matriz es una lista de listas con enteros.
    POST: 
      Retorna la matriz con cada fila ordenada en forma ascendente.
    """
    for fila in matriz:
        fila.sort()
    return matriz

# FUNCIÓN: Intercambiar dos filas de la matriz dadas sus posiciones.
def intercambiar_filas(matriz: List[List[int]], fila1: int, fila2: int) -> List[List[int]]:
    """
    CONTRATO:
    PRE: 
        fila1 y fila2 son índices válidos de filas en la matriz.
    POST: 
        Retorna la matriz con las filas fila1 y fila2 intercambiadas.
    """
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]
    return matriz

# FUNCIÓN: Intercambiar dos columnas de la matriz dadas sus posiciones.
def intercambiar_columnas(matriz: List[List[int]], col1: int, col2: int) -> List[List[int]]:
    """PRE: col1 y col2 son índices válidos de columnas en la matriz.
    POST: Retorna la matriz con las columnas col1 y col2 intercambiadas.
    """
    for fila in matriz:
        fila[col1], fila[col2] = fila[col2], fila[col1]
    return matriz

# FUNCIÓN: Trasponer la matriz sobre sí misma (intercambiar Aij por Aji).
def trasponer_matriz(matriz: List[List[int]]) -> List[List[int]]:
    """PRE: matriz es una lista de listas cuadrada.
    POST: Retorna la matriz transpuesta sobre sí misma.
    """
    N = len(matriz)
    for i in range(N):
        for j in range(i + 1, N):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]
    return matriz

# FUNCIÓN: Calcular el promedio de los elementos de una fila.
def promedio_fila(matriz: List[List[int]], fila: int) -> float:
    """
    CONTRATO:
    PRE:
        fila es un índice válido para la matriz.
    POST: 
        Retorna el promedio de los elementos de la fila especificada.
    """
    return sum(matriz[fila]) / len(matriz[fila])

# FUNCIÓN: Calcular el porcentaje de elementos impares en una columna.
def porcentaje_impares_columna(matriz: List[List[int]], columna: int) -> float:
    """
    CONTRATO:
    PRE: 
        columna es un índice válido para las columnas de la matriz.
    POST: 
        Retorna el porcentaje de elementos impares en la columna especificada.
    """
    total = len(matriz)
    impares = sum(fila[columna] % 2 != 0 for fila in matriz)
    return (impares / total) * 100

# FUNCIÓN: Determinar si la matriz es simétrica respecto a su diagonal principal.
def es_simetrica_diagonal_principal(matriz: List[List[int]]) -> bool:
    """PRE: 
        matriz es una lista de listas cuadrada.
    POST: 
        Retorna True si la matriz es simétrica respecto a la diagonal principal, False en caso contrario.
    """
    N = len(matriz)
    return all(matriz[i][j] == matriz[j][i] for i in range(N) for j in range(N))

# FUNCIÓN: Determinar si la matriz es simétrica respecto a su diagonal secundaria.
def es_simetrica_diagonal_secundaria(matriz: List[List[int]]) -> bool:
    """PRE: 
        matriz es una lista de listas cuadrada.
    POST: 
        Retorna True si la matriz es simétrica respecto a su diagonal secundaria, False en caso contrario.
    """
    N = len(matriz)
    return all(matriz[i][j] == matriz[N - 1 - i][N - 1 - j] for i in range(N) for j in range(N))

# FUNCIÓN: Determinar qué columnas de la matriz son palíndromos (capicúas).
def columnas_palindromas(matriz: List[List[int]]) -> List[int]:
    """PRE: matriz es una lista de listas cuadrada.
    POST: Retorna una lista con los índices de las columnas que son palíndromos.
    """
    N = len(matriz)
    return [col for col in range(N) if (columna := [matriz[row][col] for row in range(N)]) == columna[::-1]]

# FUNCIÓN: Imprimir la matriz.
def imprimir_matriz(matriz: List[List[int]]) -> None:
    """PRE: 
        matriz es una lista de listas con elementos imprimibles.
    POST:   
        Imprime la matriz en formato de lista de listas.
    """
    for fila in matriz:
        print(fila)

def main() -> None:
    """
    CONTRATO:
    PRE:
     Se espera que el usuario ingrese un valor entero positivo N para el tamaño de la matriz.
     El usuario debe ingresar índices válidos para las operaciones de intercambio de filas y columnas.
     Se asume que la entrada del usuario para índices y cálculos es válida y está dentro del rango de la matriz.
    
    POST:
     Imprime la matriz inicial, la matriz después de ordenar filas, la matriz después de intercambiar filas y columnas, y la matriz traspuesta.
     Imprime el promedio de los elementos de una fila especificada.
     Imprime el porcentaje de elementos impares en una columna especificada.
     Imprime si la matriz es simétrica respecto a la diagonal principal y secundaria.
     Imprime los índices de las columnas que son palíndromas.
    """
    # Leer el valor de N
    N = int(input("Ingrese el valor de N (tamaño de la matriz N x N): "))
    
    # Cargar la matriz
    matriz = cargar_matriz(N)
    
    # Imprimir la matriz cargada
    print("Matriz cargada:")
    imprimir_matriz(matriz)
    
    # Ordenar las filas
    matriz = ordenar_filas(matriz)
    print("\nMatriz después de ordenar las filas:")
    imprimir_matriz(matriz)
    
    # Intercambiar filas
    fila1 = int(input("\nIngrese el índice de la primera fila para intercambiar: "))
    fila2 = int(input("Ingrese el índice de la segunda fila para intercambiar: "))
    matriz = intercambiar_filas(matriz, fila1, fila2)
    print("\nMatriz después de intercambiar las filas:")
    imprimir_matriz(matriz)
    
    # Intercambiar columnas
    col1 = int(input("\nIngrese el índice de la primera columna para intercambiar: "))
    col2 = int(input("Ingrese el índice de la segunda columna para intercambiar: "))
    matriz = intercambiar_columnas(matriz, col1, col2)
    print("\nMatriz después de intercambiar las columnas:")
    imprimir_matriz(matriz)
    
    # Trasponer la matriz
    matriz = trasponer_matriz(matriz)
    print("\nMatriz después de trasponerla:")
    imprimir_matriz(matriz)
    
    # Calcular el promedio de una fila
    fila_promedio = int(input("\nIngrese el número de la fila para calcular su promedio: "))
    promedio = promedio_fila(matriz, fila_promedio)
    print(f"\nPromedio de los elementos de la fila {fila_promedio}: {promedio}")
    
    # Calcular porcentaje de impares en una columna
    col_porcentaje = int(input("\nIngrese el número de la columna para calcular el porcentaje de elementos impares: "))
    porcentaje_impares = porcentaje_impares_columna(matriz, col_porcentaje)
    print(f"\nPorcentaje de elementos impares en la columna {col_porcentaje}: {porcentaje_impares}%")
    
    # Verificar simetría respecto a la diagonal principal
    simetrica_principal = es_simetrica_diagonal_principal(matriz)
    print(f"\nLa matriz es simétrica respecto a la diagonal principal: {simetrica_principal}")
    
    # Verificar simetría respecto a la diagonal secundaria
    simetrica_secundaria = es_simetrica_diagonal_secundaria(matriz)
    print(f"\nLa matriz es simétrica respecto a la diagonal secundaria: {simetrica_secundaria}")
    
    # Determinar columnas palíndromas
    columnas_palindromas_list = columnas_palindromas(matriz)
    print(f"\nÍndices de las columnas palíndromas: {columnas_palindromas_list}")

if __name__ == "__main__":
    main()
