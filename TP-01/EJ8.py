"""La siguiente función permite averiguar el día de la semana para una fecha determinada.
 La fecha se suministra en forma de tres parámetros enteros y la función devuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para
imprimir por pantalla el calendario de un mes completo, correspondiente a un mes
y año cualquiera basándose en la función suministrada. Considerar que la semana
comienza en domingo."""

from functools import reduce

# Función lambda para determinar si un año es bisiesto
es_bisiesto = lambda año: (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)


# FUNCIÓN: dia_de_la_semana
def dia_de_la_semana(dia: int, mes: int, year: int) -> int:
    """
    Calcula el día de la semana para una fecha dada.

    CONTRATO:
    PRE:
        dia: (int), valor entre 1 y 31 (según el mes y año).
        mes: (int), valor entre 1 y 12.
        year: (int), valor mayor o igual a 0.

    POST:
        Devuelve un int entre 0 y 6 donde:
             0 representa domingo
             1 representa lunes
             2 representa martes
             ...
             6 representa sábado
    """
    if mes < 3:
        mes += 12
        year -= 1
    siglo = year // 100
    anio2 = year % 100
    diasem = (
        ((26 * (mes + 1) - 2) // 10)
        + dia
        + anio2
        + (anio2 // 4)
        + (siglo // 4)
        - (2 * siglo)
    ) % 7
    return diasem if diasem >= 0 else diasem + 7


# FUNCIÓN: dias_del_mes
def dias_del_mes(mes: int, year: int) -> int:
    """
    Devuelve el número de días en un mes específico considerando si es bisiesto.

    CONTRATO:
    PRE:
        mes: int, valor entre 1 y 12.
        year: int, valor mayor o igual a 0.

    POST:
        Devuelve el número de días en el mes especificado. Los valores posibles son 28, 30 o 31.
    """
    if mes in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif mes in {4, 6, 9, 11}:
        return 30
    elif mes == 2:
        return 29 if es_bisiesto(year) else 28


# FUNCIÓN: armar_mes
def armar_mes(dia: int, dias: int) -> list:

    """ Genera una lista de días del mes con espacios iniciales utilizando lambda.

    CONTRATO:
    PRE:
        dia: (int), valor entre 0 y 6, representa el día de la semana en el que comienza el mes.
        dias: (int), valor entre 28 y 31, representa el número de días en el mes.

    POST:
        Devuelve una lista de enteros donde los primeros 'dia' elementos son ceros
        (representan los espacios vacíos antes del primer día del mes) 
        y los siguientes elementos son los días del mes, comenzando con 1 y terminando con 'dias'. 
    """
    generar_dias = lambda dia, dias: [0] * dia + list(range(1, dias + 1))
    return generar_dias(dia, dias)


# FUNCIÓN: imprimir_mes
def imprimir_mes(mes: list, nombre_mes: str, year: int) -> None:
    """
    Imprime el calendario de un mes completo.

    CONTRATO:
    PRE:
        mes: list de enteros, representa los días del mes y los espacios vacíos al principio.
        nombre_mes: (str), nombre del mes (por ejemplo, "Enero").
        year: (int), valor mayor o igual a 0, representa el año.

    POST:
        Imprime el calendario del mes en la consola en formato de texto, donde cada fila representa una semana.
    """
    print(f"\n-- {nombre_mes} de {year} --")
    print(" ".join(semana))
    print("-" * (len(semana) * 4))

    dias_formateados = [f"{d:>2}" if d else "  " for d in mes]

    for i in range(0, len(dias_formateados), 7):
        semana_actual = dias_formateados[i:i + 7]
        print(" ".join(semana_actual))

    print("-" * (len(semana) * 4))


# FUNCION: main
def main() -> None:
    """
    Función principal para gestionar la entrada del usuario y generar el calendario.

    CONTRATO:
    PRE:
        - No requiere parámetros de entrada.

    POST:
        - Solicita al usuario que ingrese el número del mes y el año.
        - Llama a las funciones "dia_de_la_semana", "dias_del_mes", "armar_mes", y "imprimir_mes" para generar y
          mostrar el calendario del mes seleccionado.
    """
    mes = int(input("Ingrese el número de mes (1-12): "))
    year = int(input("Ingrese el año: "))
    dia = dia_de_la_semana(1, mes, year)
    dias = dias_del_mes(mes, year)
    lista_mes = armar_mes(dia, dias)
    nombre_mes = meses[mes - 1]
    imprimir_mes(lista_mes, nombre_mes, year)


# Definiciones globales
meses = (
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
)
semana = ("DOM", "LUN", "MAR", "MIE", "JUE", "VIE", "SAB")

if __name__ == "__main__":
    main()
