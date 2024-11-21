# Trabajo Práctico 5: Manejo de excepciones

""" La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
módulo math. Escribir un programa que utilice esta función para calcular la raíz
cuadrada de un número cualquiera ingresado a través del teclado. El programa
debe utilizar manejo de excepciones para evitar errores si se ingresa un número
negativo."""


# FUNCIÓN: calcular_raiz_cuadrada
def calcular_raiz_cuadrada() -> float:
    """
    Solicita un número al usuario y calcula su raíz cuadrada.

    PRE: El número ingresado debe ser mayor o igual a 0.
    POST: Retorna la raíz cuadrada del número ingresado.
    """
    while True:
        try:
            numero = float(input("Ingrese un número para calcular su raíz cuadrada: "))
            if numero < 0:
                raise ValueError(
                    "No se puede calcular la raíz cuadrada de un número negativo."
                )
            raiz = numero**0.5
            return raiz
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese un número válido.")


# FUNCIÓN: principal
def main() -> None:
    """
    Función principal que ejecuta el cálculo de la raíz cuadrada.

    PRE: Ninguno.
    POST: No retorna nada. Muestra la raíz cuadrada del número ingresado.
    """
    resultado = calcular_raiz_cuadrada()
    print(f"La raíz cuadrada es: {resultado}")


if __name__ == "__main__":
    main()
