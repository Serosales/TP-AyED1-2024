# Trabajo Práctico 8: Tuplas, conjuntos y diccionarios

"""Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras
ordenadas según su longitud. Los signos de puntuación no deben afectar el
proceso """


def procesar_frase(frase: str) -> set:
    """
    Procesa una frase eliminando palabras repetidas y los signos de puntuación.

    Pre:
    La frase es una cadena de texto que puede contener palabras y signos de puntuación.

    Post:
    Retorna un conjunto con las palabras únicas de la frase, sin signos de puntuación.
    """
    # Definir los signos de puntuación a eliminar
    signos_puntuacion = ".,!?;:()[]{}'\"-"

    # Eliminar los signos de puntuación de la frase
    frase_limpia = "".join(
        caracter for caracter in frase if caracter not in signos_puntuacion
    )

    # Convertir la frase en una lista de palabras, separadas por espacios
    palabras = frase_limpia.split()

    # Crear un conjunto con las palabras (esto elimina las palabras repetidas)
    return set(palabras)


def ordenar_por_longitud(palabras: set) -> list:
    """
    Ordena un conjunto de palabras según su longitud de menor a mayor.

    Pre:
    Las palabras es un conjunto de cadenas de texto.

    Post:
    Retorna una lista de palabras ordenadas según su longitud.
    """
    return sorted(palabras, key=len)


def main() -> None:
    """
    Pre:
    El usuario debe ingresar una cadena de texto (frase) que puede contener palabras y signos de puntuación.
    La frase puede tener palabras repetidas y signos de puntuación.

    Post:
    Se eliminan las palabras repetidas.
    Los signos de puntuación se eliminan correctamente.
    Se imprime una lista de palabras únicas ordenadas por su longitud de menor a mayor.
    """
    # Solicitar al usuario ingresar una frase
    frase = input("Ingrese una frase: ")

    # Procesar la frase para eliminar palabras repetidas y signos de puntuación
    palabras_unicas = procesar_frase(frase)

    # Ordenar las palabras por longitud
    palabras_ordenadas = ordenar_por_longitud(palabras_unicas)

    # Mostrar las palabras ordenadas
    print("Palabras ordenadas por longitud:")
    for palabra in palabras_ordenadas:
        print(palabra)


if __name__ == "__main__":
    main()
