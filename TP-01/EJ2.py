"""2. Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no. Realizar también un
programa para verificar el comportamiento de la función"""


# FUNCIÓN: es_anio_bisiesto
def es_anio_bisiesto(anio: int) -> bool:
    """
    CONTRATO:
    PRE::
        "anio" debe ser un entero positivo que representa el año a verificar.
    POST:
        Devuelve True si el año es bisiesto.
        Devuelve False si el año no es bisiesto.

    """

    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


# FUNCIÓN:es_fecha_valida
def es_fecha_valida(dia: int, mes: int, anio: int) -> bool:
    """
    CONTRATO:
    PRE:
    - "dia", "mes" y "anio" deben ser enteros positivos donde "dia" y "mes" son mayores que 0,
      y "mes" debe estar en el rango de 1 a 12.
    - "anio" debe ser un entero positivo.

    POST:
        Devuelve True si la combinación de "dia", "mes", y "anio" corresponde a una fecha válida.
        Devuelve False si la combinación no representa una fecha válida.
    """
    # Días del mes que no son bisiestos.
    """  
    dias_por_mes = ENERO;FEBRERO;MARZO;ABRIL;MAYO;JUNIO;JULIO;AGOSTO;SEPTIEMBRE;OCTBRE;NOVIEMBRE;DICIEMBRE.
    """
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #  Día de febrero que es bisiesto,cuando febrero tiene 29 días.
    """UNICAMENTE FEBRERO."""
    if es_anio_bisiesto(anio):
        dias_por_mes[1] = 29

    # Verificar si el mes es válido
    elif mes < 1 or mes > 12:
        return False

    # Verificar si el día es válido para el mes.

    if dia < 1 or dia > dias_por_mes[mes - 1]:
        return False

    return True


# FUNCIÓN: ingrese_los_numeros
def ingrese_los_numeros() -> tuple:
    """
    CONTRATO:
     PRE:
        Se asume que el usuario ingresará valores enteros para día, mes y año.

    POST:
        Devuelve una tupla (dia, mes, anio) donde "dia", "mes" y "anio" son enteros positivos
        ingresados por el usuario.

    """
    # Solicitar el ingreso por teclado de dia,mes y año.
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))

    return (dia, mes, anio)


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
    dia, mes, anio = ingrese_los_numeros()

    if es_fecha_valida(dia, mes, anio):
        print("La fecha es válida.")
    else:
        print("La fecha no es válida.")


if __name__ == "__main__":
    main()
