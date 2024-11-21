# Trabajo Práctico 5: Manejo de excepciones

""" . Desarrollar una función que devuelva una cadena de caracteres con el nombre del
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
Devolver una cadena vacía si el número de mes es inválido. La detección de meses
inválidos deberá realizarse a través de excepciones.
"""


# FUNCIÓN: Obtener el nombre del mes según su número
def obtener_nombre_del_mes(mes_numero: int) -> str:
    """
    PRE:
        mes_numero (int): Número entero entre 1 y 12 representando un mes del año.
    POST:
        Retorna el nombre del mes correspondiente al número dado.
        Si el número no es válido, retorna una cadena vacía.
    """
    nombres_meses = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ]

    # Verificar si el número de mes está dentro del rango válido
    if 1 <= mes_numero <= 12:
        return nombres_meses[mes_numero - 1]
    return ""


# FUNCIÓN: Programa principal para ejecutar la función
def main() -> None:
    """
    PRE:
        No requiere parámetros. Solicita al usuario ingresar un número de mes entre 1 y 12.
    POST:
        Muestra el nombre del mes correspondiente si el número es válido.
        Si el número no es válido o no es entero, muestra un mensaje de error.
    """
    try:
        mes_numero = int(input("Ingrese un número de mes (1-12): "))
        nombre_mes = obtener_nombre_del_mes(mes_numero)

        if nombre_mes:
            print(f"El mes correspondiente es: {nombre_mes}")
        else:
            print("Error: El número de mes ingresado es inválido.")
    except ValueError:
        print("Error: Debe ingresar un número entero.")


if __name__ == "__main__":
    main()
