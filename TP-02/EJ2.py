""" Escribir funciones para:
a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa
a través del teclado.
b. Recibir una lista como parámetro y devolver True si la misma contiene algún
elemento repetido. La función no debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
únicos de la lista original, sin importar el orden.
Combinar estas tres funciones en un mismo programa."""

import random as rn

rn.seed(100)


# FUNCION: generar_lista_aleatoria
def generar_lista_aleatoria(N):
    """Genera una lista de N números aleatorios del 1 al 100.
    CONTRATO:
    PRE:
    - N debe ser un número entero positivo.

    POST:
    - Devuelve una lista de longitud N que contiene números enteros aleatorios entre 1 y 100.
    """
    return [rn.randint(1, 100) for _ in range(N)]


# FUNCION:contiene_repetidos
def contiene_repetidos(lista: list) -> list:
    """Devuelve True si la lista contiene algún elemento repetido.
     CONTRATO:
    PRE:
    - lista debe ser una lista de números (se espera una lista no vacía).

    POST:
    - Devuelve True si la lista contiene al menos un número que aparece más de una vez.
    - Devuelve False si todos los elementos de la lista son únicos.
    """
    return any(lista.count(x) > 1 for x in lista)


# FUNCION: obtener_elementos_unicos
def obtener_elementos_unicos(lista: list) -> list:
    """Devuelve una nueva lista con los elementos únicos de la lista original.
     CONTRATO:
    PRE:
    - lista debe ser una lista de números.

    POST:
    - Devuelve una nueva lista que contiene solo los elementos que aparecen exactamente una vez en la lista original.
    - La longitud de la lista resultante puede ser menor o igual que la longitud de la lista original, pero nunca mayor.
    """
    return list(filter(lambda x: lista.count(x) == 1, lista))


# FUNCION:main
def main() -> None:
    """
     CONTRATO:
    PRE:
    - El usuario debe ingresar un número entero positivo cuando se le solicite.

    POST:
    - Genera una lista de números aleatorios y la imprime.
    - Informa si la lista contiene elementos repetidos.
    - Imprime una lista con los elementos únicos de la lista original.
    - No tiene parámetro de retorno.
    """

    # a. Generar una lista de números aleatorios
    N = int(input("Ingrese la cantidad de números aleatorios a generar: "))
    lista = generar_lista_aleatoria(N)
    print("Lista generada:", lista)

    # b. Verificar si la lista contiene elementos repetidos
    tiene_repetidos = contiene_repetidos(lista)
    print("La lista contiene elementos repetidos:", tiene_repetidos)

    # c. Obtener una nueva lista con los elementos únicos
    lista_unicos = obtener_elementos_unicos(lista)
    print("Lista con elementos únicos:", lista_unicos)


if __name__ == "__main__":
    main()
