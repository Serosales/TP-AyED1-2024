# Trabajo Práctico 8: Tuplas, conjuntos y diccionarios

""" Escribir una función que reciba como parámetro una tupla conteniendo una fecha
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
en formato extendido. La función debe contemplarse que el año se ingrese en dos
dígitos, los que serán interpretados según un año de corte definido dentro del
programa. Cualquier año mayor que éste se considerará del siglo pasado. Por
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030"
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de
1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y
mostrar el resultado."""


def fecha_formato_extendido(fecha: tuple) -> str:
    """
    Recibe una tupla con una fecha (día, mes, año) y devuelve una cadena de caracteres
    con la fecha expresada en formato extendido.

    Pre:
    Recibe como parámetro una tupla (día, mes, año). El año puede ser de dos o cuatro dígitos.

    Post:
    Retorna una cadena de texto con la fecha en formato extendido: "Día de Mes de Año".
    Si el año es de dos dígitos, se interpreta según un año de corte (30). Si es mayor que el corte,
    se considera del siglo XXI; de lo contrario, se considera del siglo XX.
    """
    day, month, year = fecha
    year_of_cut = 30

    # Diccionario de los meses
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }

    # Si el año tiene dos dígitos, lo interpretamos según el año de corte
    if year < 100:
        if year <= year_of_cut:
            year = 2000 + year
        else:
            year = 1900 + year

    # Si el año tiene cuatro dígitos, lo dejamos tal como está
    fecha_extendida = f"{day} de {meses[month]} de {year}"

    return fecha_extendida


def ingresar_datos() -> tuple:
    """
    Solicita al usuario que ingrese una fecha (día, mes, año) y la valida.

    Pre:
    No se asume ninguna precondición específica.

    Post:
    Retorna una tupla con los valores del día, mes y año ingresados.
    Si los datos son inválidos, solicita nuevamente la entrada.
    """
    while True:
        try:
            day = int(input("Ingrese DÍA (Los días deben de ser entre 1 y 31): "))
            month = int(input("Ingrese MES (Los meses deben de ser entre 1 y 12): "))
            year = int(
                input("Ingrese AÑO (puede ser de 2 o 4 dígitos): ")
            )  # El año debe tener entre 2 y 4 dígitos

            # Validación de los días y meses
            if not (1 <= day <= 31):
                raise ValueError("El día debe estar entre 1 y 31.")
            if not (1 <= month <= 12):
                raise ValueError("El mes debe estar entre 1 y 12.")

            # Validación de los años: Deben ser válidos y de entre 2 y 4 dígitos
            if not (1 <= year <= 9999):
                raise ValueError("El año debe ser un valor numérico válido.")

            return day, month, year
        except ValueError as e:
            print(f"Error: {e}. Intenta nuevamente.")


def main() -> None:
    """
    Función principal que solicita al usuario una fecha y muestra la fecha en formato extendido.

    Pre:
    El usuario debe ingresar una fecha válida (día, mes y año).

    Post:
    Muestra la fecha en formato extendido o un mensaje de error si los datos son inválidos.
    """
    # Ingresar los datos
    fecha = ingresar_datos()

    # Convertir la fecha a formato extendido
    fecha_formateada = fecha_formato_extendido(fecha)

    # Mostrar el resultado
    print(f"La misma fecha en formato extendido es: {fecha_formateada}")


if __name__ == "__main__":
    main()
