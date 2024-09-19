"""4. Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En
qué cambiaría la función si el rango de valores fuese diferente?"""

"""4. Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En
qué cambiaría la función si el rango de valores fuese diferente?"""

# FUNCIÓN: convertir_a_romano
def convertir_a_romano(numero: int) -> str:
    """
    CONTRATO:
    PRE:
    "numero" debe ser un entero entre 0 y 3999 inclusive.
    POST:
    Devuelve una cadena con la representación romana del número.
    """

    valores_simbolos = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    resultado = "".join(
        simbolo * (numero // valor)
        for valor, simbolo in valores_simbolos
        if (numero := numero % valor) or True
    )
    return resultado


# FUNCIÓN: main
def main():
    """
    CONTRATO:
    PRE:
    Se espera que el usuario ingrese un número entero.
    POST:
    Si el número está en el rango de 0 a 3999, se imprime su representación romana.
    De lo contrario, se muestra un mensaje de error.
    """

    # Solicitar un número al usuario
    numero = int(input("Ingrese un número entre 0 y 3999: "))
    if 0 <= numero <= 3999:
        romano = convertir_a_romano(numero)
        print(f"{numero} en romano es: {romano}")
    else:
        print("El número ingresado no está en el rango permitido.")


if __name__ == "__main__":
    main()
