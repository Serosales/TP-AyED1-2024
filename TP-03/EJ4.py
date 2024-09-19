"""Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas
en cada una de sus plantas durante una semana. De este modo, cada columna representa el día de la semana y cada fila a una de sus fábricas. Ejemplo:
"""

""" Se solicita:
a. Crear una matriz con datos generados al azar para N fábricas durante una
semana, considerando que la capacidad máxima de fabricación es de 150
unidades por día y puede suceder que en ciertos días no se fabrique ninguna.

b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica.

c. Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).

d. Cuál es el día más productivo, considerando todas las fábricas combinadas.

e. Crear una lista por comprensión que contenga la menor cantidad fabricada
por cada fábrica."""

import random as rn

# FUNCIÓN: generar_matriz
def generar_matriz(N: int) -> list[list[int]]:
    """
    CONTRATO:
    PRE: 
        N es un entero positivo que representa el número de fábricas.
    POST: 
        Retorna una matriz de tamaño N x 7, con valores enteros aleatorios entre 0 y 150.
    """
    return [[rn.randint(0, 150) for _ in range(7)] for _ in range(N)]


# FUNCIÓN: imprimir_matriz
def imprimir_matriz(matriz: list[list[int]]) -> None:
    """
    CONTRATO:
    PRE: 
        matriz es una lista de listas de enteros, representando una matriz.
    POST: 
        Imprime la matriz en la consola, donde cada fila se muestra en una línea separada.
    """
    for fila in matriz:
        print(" ".join(map(str, fila)))


# FUNCIÓN: total_por_fabrica
def total_por_fabrica(matriz: list[list[int]]) -> dict[str, int]:
    """
    CONTRATO:
    PRE: matriz es una lista de listas de enteros, representando una matriz de producción.
    POST: Retorna un diccionario donde las llaves son las fábricas (en formato 'Fábrica i') y los valores son el total de bicicletas fabricadas por cada fábrica.
    """
    return {f"Fábrica {i+1}": sum(fila) for i, fila in enumerate(matriz)}


# FUNCIÓN: fabrica_mas_productiva_en_un_dia
def fabrica_mas_productiva_en_un_dia(matriz: list[list[int]]) -> tuple[int, int, int]:
    """
    CONTRATO:
    PRE: 
        matriz es una lista de listas de enteros, representando una matriz de producción.
    POST: 
        Retorna una tupla con tres valores: el número de la fábrica (1-indexado), el día (1-indexado) y la cantidad máxima producida en un solo día.
    """
    # Encuentra la máxima producción en un solo día utilizando comprensión de listas
    max_produccion = max(produccion for fila in matriz for produccion in fila)
    
    # Encuentra la fábrica y el día correspondiente a la máxima producción
    fabrica, dia = next(
        (i, j) for i, fila in enumerate(matriz) 
        for j, produccion in enumerate(fila) 
        if produccion == max_produccion
    )

    return fabrica + 1, dia + 1, max_produccion

# FUNCIÓN: dia_mas_productivo
def dia_mas_productivo(matriz: list[list[int]]) -> tuple[int, int]:
    """
    CONTRATO:
    PRE: 
        matriz es una lista de listas de enteros, representando una matriz de producción.
    POST: 
        Retorna una tupla con dos valores: el día más productivo (1-indexado) y la cantidad total de bicicletas producidas en ese día por todas las fábricas.
    """
    totales_dia = [sum(fila[j] for fila in matriz) for j in range(7)]
    dia_max = totales_dia.index(max(totales_dia))
    return dia_max + 1, max(totales_dia)  # sumamos 1 para hacer la numeración amigable


# FUNCIÓN: menor_cantidad_por_fabrica
def menor_cantidad_por_fabrica(matriz: list[list[int]]) -> dict[str, int]:
    """
    CONTRATO:
    PRE: 
        matriz es una lista de listas de enteros, representando una matriz de producción.
    POST: 
        Retorna un diccionario donde las llaves son las fábricas (en formato 'Fábrica i') y los valores son la menor cantidad fabricada por cada fábrica.
    """
    return {f"Fábrica {i+1}": min(fila) for i, fila in enumerate(matriz)}


def main():
    N = int(input("Ingrese el número de fábricas: "))

    if N <= 0:
        print("El número de fábricas debe ser mayor que 0.")
        return

    matriz = generar_matriz(N)

    print("\nMatriz de producción:")
    imprimir_matriz(matriz)

    totales_fabrica = total_por_fabrica(matriz)
    print("\nTotal de bicicletas fabricadas por cada fábrica:")
    for fabrica, total in totales_fabrica.items():
        print(f"{fabrica}: {total} bicicletas")

    fabrica, dia, produccion = fabrica_mas_productiva_en_un_dia(matriz)
    print(
        f"\nLa fábrica {fabrica} produjo más en un solo día con {produccion} bicicletas en el día {dia}."
    )

    dia_max, produccion_max = dia_mas_productivo(matriz)
    print(
        f"\nEl día más productivo es el día {dia_max} con {produccion_max} bicicletas producidas en total."
    )

    menores_por_fabrica = menor_cantidad_por_fabrica(matriz)
    print("\nMenor cantidad fabricada por cada fábrica:")
    for fabrica, cantidad in menores_por_fabrica.items():
        print(f"{fabrica}: {cantidad} bicicletas")


if __name__ == "__main__":
    main()
