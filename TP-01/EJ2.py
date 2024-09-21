"""2. Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no. Realizar también un
programa para verificar el comportamiento de la función"""


# FUNCIÓN: leap_year (año bisiesto)
def leap_year(year: int) -> bool:
    """
    CONTRATO:
    PRE::
        "year " debe ser un entero positivo que representa el año a verificar.
    POST:
        Devuelve True(boolean) si el año es bisiesto.
        Devuelve False(boolean) si el año no es bisiesto.

    """

    return (year % 4 == 0 and year  % 100 != 0) or (year % 400 == 0)


# FUNCIÓN:(fecha valida)
def valid_date(day: int, month: int, year: int) -> bool:
    """
    CONTRATO:
    PRE:
    - "day"(int), "month"(int) y "year"(int) deben ser enteros positivos donde "day" y "month" son mayores que 0,
      y "month" debe estar en el rango de 1 a 12.
    - "year" debe ser un entero positivo.

    POST:
        Devuelve True(boolean) si la combinación de "day", "month", y "year" corresponde a una fecha válida.
        Devuelve False(boolean) si la combinación no representa una fecha válida.
    """
    # Días del mes que no son bisiestos.
    """  
    dias_por_mes = ENERO  31 días ;FEBRERO 28 días  ;MARZO 31 días ;ABRIL 30 días;MAYO 31 días ;JUNIO 30 días;
    JULIO 31 días ;AGOSTO 31 días ;SEPTIEMBRE 30  dias ;OCTBRE 31 dias ;NOVIEMBRE 30 días ;DICIEMBRE 31 días .
    """
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #  Día de febrero que es bisiesto,cuando febrero tiene 29 días.
    """UNICAMENTE FEBRERO."""
    if leap_year(year):
        dias_por_mes[1] = 29

    # Verificar si el mes es válido
    elif month < 1 or month> 12:
        return False

    # Verificar si el día es válido para el mes.

    if day < 1 or day > dias_por_mes[month - 1]:
        return False

    return True


# FUNCIÓN: ingrese_los_numeros
def enter_numbers() -> tuple[int,int,int]:
    """
    CONTRATO:
     PRE:
        Se asume que el usuario ingresará valores enteros para día, mes y año.

    POST:
        Devuelve una tupla (dia, mes, anio) donde "dia", "mes" y "anio" son enteros positivos
        ingresados por el usuario.

    """
    # Solicitar el ingreso por teclado de dia,mes y año.
    d = int(input("Ingrese el día: "))
    m = int(input("Ingrese el mes: "))
    y = int(input("Ingrese el año: "))

    return (d, m, y)


# FUNCIÓN: main
def main() -> None:
    """
    CONTRATO:
    PRE:
        Función "main".
    POST:
        Imprime un mensaje indicando si la fecha  es válida o no.
        No tiene parametros de retorno.
    """
    dia, mes, anio = enter_numbers()

    if valid_date(dia, mes, anio):
        print("La fecha es válida.")
    else:
        print("La fecha no es válida.")


if __name__ == "__main__":
    main()
