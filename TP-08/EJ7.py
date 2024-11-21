# Trabajo Práctico 8: Tuplas, conjuntos y diccionarios

""" Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
usuario y eliminarlos del conjunto mediante el método remove, mostrando el contenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos
inexistentes """


def main() -> None:
    """
    Función principal que gestiona la eliminación de elementos de un conjunto de números enteros del 0 al 9.

    Pre:
    El conjunto inicial contiene los números enteros entre 0 y 9.

    Post:
    El usuario puede ingresar un número para eliminarlo del conjunto.
    Si el número no está en el conjunto, se muestra un mensaje de error.
    Si la entrada no es válida (no es un número entero), se muestra un mensaje pidiendo un número válido.
    El proceso termina cuando el usuario ingresa -1.
    Los errores inesperados son capturados y notificados al usuario.
    Esta función no retorna ningún valor
    """
    # Definir un conjunto con números enteros entre 0 y 9
    conjunto: set[int] = set(range(10))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    print("Conjunto inicial:", conjunto)

    while True:
        # Solicitar al usuario un número para eliminar
        entrada: str = input(
            "Ingrese un número para eliminar del conjunto (o -1 para salir): "
        )

        try:
            # Intentar convertir la entrada a un número entero
            numero: int = int(entrada)

            # Si el número es -1, finalizar el proceso
            if numero == -1:
                print("Finalizando el proceso.")
                break

            # Intentar eliminar el número del conjunto
            conjunto.remove(numero)
            print(f"Número {numero} eliminado. Conjunto actual: {conjunto}")

        except KeyError:
            # En caso de que el número no esté en el conjunto
            print(f"Error: El número {numero} no está en el conjunto.")
        except ValueError:
            # En caso de que la entrada no sea un número válido
            print("Por favor, ingrese un número entero válido.")
        except Exception as e:
            # Captura cualquier otra excepción que pueda ocurrir
            print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    main()
