"""Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
ni agregados, desarrollar programas que permitan:
a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera."""


# FUNCIÓN dia_siguiente:
def dia_siguiente(day: int, month: int, year: int) -> tuple[int, int, int]:
    """Devuelve el día siguiente a la fecha dada.

    CONTRATO:
     PRE:
        day es un entero que representa el día del mes.
        month es un entero que representa el mes del año.
        year es un entero que representa el año.
     POST:
         Devuelve una tupla (day, month, year) que representa la fecha del día siguiente.
         Si el día supera el número de días del mes, se ajusta al siguiente mes.
         Si el mes supera el número de meses en el año, se ajusta al siguiente año.
    """
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        dias_mes[1] = 29

    day+= 1
    if day > dias_mes[month - 1]:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1

    return (day, month, year)


# FUNCIÓN sumar_dia:
def sumar_dias(day: int, month: int, year: int, n: int) -> tuple[int, int, int]:
    """Suma N días a la fecha dada.

    CONTRATO:
     PRE:
       "dia" es un entero que representa el día del mes (1 <= d <= 31).
       "mes"es un entero que representa el mes del año (1 <= m <= 12).
       "year" es un entero que representa el año (a > 0).
        "n"  es un entero positivo que representa el número de días a sumar (n >= 0).
     POST:
      - Devuelve una tupla (dia, mes, year) que representa la fecha resultante después de sumar N días.
    """
    for _ in range(n):
        day, month, year = dia_siguiente(day, month, year)
    return (day, month, year)


# FUNCIÓN dias_entre_fechas:
def dias_entre_fechas(
    day_1: int, month_1: int, year_1: int, day_2: int, month_2: int, year_2: int
) -> int:
    """Calcula la cantidad de días entre dos fechas.

    CONTRATO:
     PRE:
        (day_1, month_1, year_1) es la fecha inicial, con day_1 es un entero que debe de estar entre 1 y 31.
        month_1 debe de se entre 1 y 12 (deben de ser números enteros).
        (day_2, month2, year_2) es la fecha final.
        day_2 bede de estar entre los días 1 y 31.
        month_2 debe de estar entre los meses 1 y 12.
        Para que sea valido.
     POST:
       Devuelve un entero que representa la cantidad de días entre las dos fechas.
       Si la fecha inicial es posterior a la fecha final, el resultado será un número negativo.
    """
    days = 0
    while (day_1, month_1, year_1) != (day_2, month_2, year_2):
        day_1, month_1, year_1 = dia_siguiente(day_1, month_1, year_1)
        dias += 1
        if (
            year_1 > year_2
            or (year_1 == year_2 and month_1 > month_2)
            or (year_1 == year_2 and month_1 == month_2 and day_1 > day_2)
        ):
            return -days
    return days

# FUNCIÓN obtener_fecha:
def obtener_fecha() -> tuple[int, int, int]:
    """Solicita al usuario una fecha y devuelve una tupla (día, mes, año).

    CONTRATO:
     PRE:
       El usuario proporciona valores válidos para el día, mes y año.
     POST:
       Devuelve una tupla (d, m, a) donde:
         d es el día del mes (entero positivo).
         m es el mes del año (entero entre 1 y 12).
         a es el año (entero positivo).
    """
    d = int(input("Introduce el día: "))
    m = int(input("Introduce el mes: "))
    y = int(input("Introduce el año: "))
    return (d, m, y)

# FUNCIÓN main:
def main() -> None:
    """Función principal para sumar días y calcular la diferencia entre fechas.

    CONTRATO:
     PRE:
       No se requieren precondiciones específicas, ya que la función solicita entradas al usuario.
     POST:
       Imprime la fecha resultante después de sumar una cantidad de días a la fecha inicial.
       Imprime la cantidad de días entre dos fechas proporcionadas por el usuario.
       No tiene parametros de retorno.
    """
    print("Introduce la fecha inicial:")
    day_1, month_1, year_1 = obtener_fecha()

    print("Introduce la fecha final:")
    day_2, month_2, year_2 = obtener_fecha()

    # Obtener el número de días a sumar
    dias_a_sumar = int(input("Introduce el número de días a sumar: "))

    # Sumar días
    d, m, y = sumar_dias(day_1, month_1, year_1, dias_a_sumar)
    print(f"Fecha después de sumar {dias_a_sumar} días: {d}/{m}/{y}")

    # Calcular días entre fechas
    dias_entre = dias_entre_fechas(day_1, month_1, year_1, day_2, month_2, year_2)
    print(
        f"Días entre {day_1}/{month_1}/{year_1} y {day_2}/{month_2}/{year_2}: {dias_entre}"
    )


if __name__ == "__main__":
    main()
