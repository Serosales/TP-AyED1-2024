""" Utilizar la técnica de listas por comprensión para construir una lista con todos los
números impares comprendidos entre 100 y 200.
"""

from random import randint as rn
from typing import List


# FUNCIÓN: Construye una lista con todos los números impares entre 100 y 200.
def numeros_impares() -> List[int]:
    """
    CONTRATO:
    "Genera una lista de números impares comprendidos entre 100 y 200 usando listas por comprensión.

    PRE:
        No se requieren entradas.
        EL rango de los numeros(int) debe de ser entre los números 100 y 200.
    POST:
        Devuelve una lista de números impares entre 100 y 200.
    """
    # Utiliza una comprensión de listas y lambda para obtener números impares
    return list(filter(lambda x: x % 2 != 0, [rn(100, 200) for _ in range(100)]))


# FUNCIÓN:main
def main() -> None:
    """
    CONTRATO:
         Genera y muestra la lista de números impares(aleatorios) entre 100 y 200.
    PRE:
        Se definen los límites para generar los números impares.
    POST:
        Llama a la función "numeros_impares" y muestra la lista generada.
        No tiene parametros de retorno.
    """

    # Llama a la función para obtener la lista de números impares
    resultado = numeros_impares()

    # Imprime el resultado
    print(f"Números impares entre 100 y 200: {resultado}")


if __name__ == "__main__":
    main()
