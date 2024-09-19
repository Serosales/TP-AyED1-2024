"""3. Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes.
Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes
 (detalladas en la tabla de abajo)
se solicita desarrollar una función que reciba como parámetro la cantidad de viajes realizados en un
determinado mes y devuelva el total gastado en viajes. 
Realizar también un programa para verificar el comportamiento de la función."""

"""Cantidad de viajes     Valor del pasaje
        1 a 20            Averiguar en Internet el valor actualizado
        21 a 30            20% de descuento sobre tarifa máxima
        31 a 40            30% de descuento sobre tarifa máxima
        Más de 40          40% de descuento sobre tarifa máxima"""


# FUNCIÓN: Solicitar la cantidad de viajes al usuario
def obtener_viajes() -> int:
    """
    CONTRATO:
    PRE:
    No se requiere entrada específica.
    POST:
    Devuelve la cantidad de viajes ingresada por el usuario.
    """
    return int(input("Ingrese la cantidad de viajes realizados en el mes: "))


# FUNCIÓN: Calcular el costo total según la cantidad de viajes
def determinar_total_gasto(viajes: int, tarifa_maxima: float) -> float:
    """
    CONTRATO:
    PRE:
    viajes es un entero positivo y tarifa_maxima es un número positivo.
    POST:
    Devuelve el total calculado basado en la cantidad de viajes y el descuento.
    """

    # Definición de descuentos por rango
    rangos_descuentos = [(20, 1.0), (30, 0.8), (40, 0.7), (float("inf"), 0.6)]

    for limite, descuento in rangos_descuentos:
        if viajes <= limite:
            return viajes * tarifa_maxima * descuento  # Retorna el total calculado


# FUNCIÓN: Calcular el total de gastos en viajes de subterráneo
def calcular_gasto(viajes: int, tarifa_maxima: float) -> float:
    """
    CONTRATO:
    PRE:
    viajes es un entero positivo y tarifa_maxima es un número positivo.
    POST:
    Devuelve el total gastado en viajes basado en la cantidad de viajes y la tarifa.
    """
    return determinar_total_gasto(
        viajes, tarifa_maxima
    )  # Retorna el total desde la función secundaria


# FUNCIÓN: main
def main() -> None:
    """
    CONTRATO:
    PRE:
    No se requiere entrada específica.
    POST:
    Imprime el total gastado basado en la cantidad de viajes proporcionada por el usuario.
    No tiene parametro de retorno.
    """
    tarifa_maxima = 2.0  # Ejemplo de tarifa máxima, actualízala según corresponda
    viajes_realizados = obtener_viajes()  # Llamada a la función para obtener viajes

    total = calcular_gasto(viajes_realizados, tarifa_maxima)
    print(f"Total gastado en viajes: ${total:.2f}")


if __name__ == "__main__":
    main()
