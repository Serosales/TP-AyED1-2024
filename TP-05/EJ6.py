# Trabajo Práctico 5: Manejo de excepciones

""". El método index permite buscar un elemento dentro de una lista, devolviendo la
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
produce una excepción de tipo ValueError. Desarrollar un programa que cargue
una lista con números enteros ingresados a través del teclado (terminando con -1)
y permita que el usuario ingrese el valor de algunos elementos para visualizar la
posición que ocupan, utilizando el método index. Si el número no pertenece a la
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda """


# FUNCIÓN: ingresar_numeros
def ingresar_numeros() -> list:
    """
    Solicita al usuario ingresar números enteros y retorna la lista de números ingresados.

    PRE: Ninguno.
    POST: Retorna una lista con los números ingresados.
    """
    numeros_ingresados = []
    while True:
        numero = int(input("Ingrese un número entero (-1 para terminar): "))
        if numero == -1:
            break
        numeros_ingresados.append(numero)
    return numeros_ingresados


# FUNCIÓN: localizar_elemento
def localizar_elemento(lista: list) -> None:
    """
    Busca un número en la lista y muestra su posición.

    PRE: La lista debe contener números enteros.
    POST: No retorna nada. Imprime la posición o el error en caso de no encontrar el número.
    """
    errores_detectados = 0
    while errores_detectados < 3:
        try:
            numero_a_buscar = int(input("Ingrese un número para buscar su posición: "))
            # Utilizar el método index para buscar el número
            posicion = lista.index(numero_a_buscar)
            print(
                f"El número {numero_a_buscar} se encuentra en la posición: {posicion}"
            )
        except ValueError:
            errores_detectados += 1
            print("Error: El número no se encuentra en la lista.")
            if errores_detectados < 3:
                print(f"Intentos fallidos: {errores_detectados}/3. Intente de nuevo.")
            else:
                print(
                    "Se han alcanzado los 3 intentos fallidos. Saliendo del programa."
                )


# FUNCIÓN: principal
def main() -> None:
    """
    Función principal que organiza el flujo del programa.

    PRE: Ninguno.
    POST: No retorna nada. Ejecuta el proceso de carga de lista y búsqueda de elementos.
    """
    lista_de_numeros = ingresar_numeros()
    localizar_elemento(lista_de_numeros)


if __name__ == "__main__":
    main()
