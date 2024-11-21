# Trabajo Práctico 5: Manejo de excepciones

"""1. Desarrollar una función para ingresar a través del teclado un número natural. La
función rechazará cualquier ingreso inválido de datos utilizando excepciones y
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea
correcto. Escribir también un programa que permita probar el correcto funcionamiento de la misma  """


# FUNCIÓN: Ingresar un número natural mayor que 0
def ingresar_numero() -> int:
    """
    PRE: El número a ingresar debe ser un número natural y mayor que cero.
    POST: Devuelve el valor ingresado en caso de ser correcto.
    """
    while True:
        numero = input("Ingrese un número natural (mayor que 0): ")
        try:
            num = int(numero)
            if num <= 0:
                raise ValueError("El número debe ser mayor que 0.")
            return num
        except ValueError as e:
            print(f"Error: {e}. Por favor, intente de nuevo.")


# FUNCIÓN: Programa principal para probar la función
def main() -> None:
    """La función main permite probar el correcto funcionamiento del programa.
    PRE: El programa no requiere parámetros de entrada.
    POST: Ejecuta la función `ingresar_numero` y muestra en pantalla el número ingresado.
    """
    numero = ingresar_numero()
    print(f"El número ingresado es: {numero}")


if __name__ == "__main__":
    main()
