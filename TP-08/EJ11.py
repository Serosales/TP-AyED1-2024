# Trabajo Práctico 8: Tuplas, conjuntos y diccionarios

""" Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales
contiene, identificando la cantidad de cada una. Devolver un diccionario con los
resultados. Luego desarrollar un programa para leer una frase e invocar a la
función por cada palabra que contenga la misma. Imprimir las palabras y la
cantidad de vocales hallada. """


def contar_vocales(palabra: str) -> dict:
    """
    Cuenta las vocales en una palabra, identificando la cantidad de cada una.

    Pre:
     La palabra es una cadena de texto (str).

    Post:
     Retorna un diccionario (dict) con la cantidad de cada vocal encontrada en la palabra.
    """
    try:
        # Definimos las vocales
        vocales = "aeiou"
        # Creamos un diccionario que cuenta las vocales en la palabra
        conteo_vocales = dict((v, palabra.count(v)) for v in vocales)
        return conteo_vocales
    except Exception as e:
        # En caso de error, mostramos un mensaje y retornamos un diccionario vacío
        print(f"Error al contar las vocales en la palabra '{palabra}': {e}")
        return {}


def procesar_frase(frase: str) -> None:
    """
    Procesa una frase, invocando a la función contar_vocales() para cada palabra.

    Pre:
     La frase es una cadena de texto (str).

    Post:
     Imprime la cantidad de vocales en cada palabra de la frase. No retorna nada.
    """
    try:
        # Dividir la frase en palabras
        palabras = frase.split()

        # Procesar cada palabra
        for palabra in palabras:
            # Contamos las vocales en la palabra
            resultados = contar_vocales(palabra)
            if resultados:  # Si hay algún conteo, imprimimos el resultado
                print(f"Palabra: '{palabra}' - {resultados}")
    except Exception as e:
        # Si ocurre un error en el procesamiento de la frase, lo mostramos
        print(f"Error al procesar la frase: {e}")


def main() -> None:
    """
    Función principal para leer una frase e invocar la función contar_vocales()
    por cada palabra.

    Pre:
     El programa espera que el usuario ingrese una cadena de texto como frase.

    Post:
     Procesa la frase e imprime la cantidad de vocales de cada palabra. No retorna nada.
    """
    try:
        # Pedimos al usuario que ingrese una frase
        frase_usuario = input("Ingrese una frase: ")

        # Procesamos la frase
        procesar_frase(frase_usuario)
    except Exception as e:
        # Si ocurre algún error, lo capturamos y mostramos el mensaje
        print(f"Error en el programa: {e}")


if __name__ == "__main__":
    main()
