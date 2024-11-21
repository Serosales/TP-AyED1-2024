# Trabajo Práctico 8: Tuplas, conjuntos y diccionarios

""" 5. En geometría un vector es un segmento de recta orientado que va desde un punto
A hasta un punto B. Los vectores en el plano se representan mediante un par ordenado de números reales (x, y) llamados componentes. Para representarlos basta
con unir el origen de coordenadas con el punto indicado en sus componentes:
Dos vectores son ortogonales cuando son perpendiculares entre sí. Para determinarlo basta calcular su producto escalar y verificar si es igual a 0. Ejemplo: 
A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales
Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor
de verdad indicando si son ortogonales o no. Desarrollar también un programa que
permita verificar el comportamiento de la función"""


def son_ortogonales(v1: tuple, v2: tuple) -> bool:
    """
    Determina si dos vectores son ortogonales.

    pre:
    v1 y v2 son tuplas con dos elementos (x, y) que representan las coordenadas de los vectores en el plano.

    post:
    Devuelve True si los vectores son ortogonales (producto escalar = 0), False en caso contrario.
    """
    # Calcular el producto escalar en una línea
    return sum(x * y for x, y in zip(v1, v2)) == 0


def main() -> None:
    """
    Función principal que permite verificar si dos vectores son ortogonales.

    pre:
    El usuario ingresa las coordenadas de dos vectores en forma de tuplas de números reales (flotantes).
    La entrada de coordenadas es proporcionada por el usuario, separando los valores por espacio.

    post:
    Imprime un mensaje indicando si los vectores son ortogonales o no, en función de su producto escalar.
    No retorna ningún valor.
    """
    # Solicitar al usuario que ingrese las coordenadas de los dos vectores y usarlas directamente
    v1 = tuple(
        map(float, input("Ingrese las coordenadas del primer vector (x y): ").split())
    )
    v2 = tuple(
        map(float, input("Ingrese las coordenadas del segundo vector (x y): ").split())
    )

    # Verificar si los vectores son ortogonales
    if son_ortogonales(v1, v2):
        print(f"Los vectores {v1} y {v2} son ortogonales.")
    else:
        print(f"Los vectores {v1} y {v2} no son ortogonales.")


if __name__ == "__main__":
    main()
