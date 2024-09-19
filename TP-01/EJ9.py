""" Resolver el siguiente problema utilizando funciones:
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso
de alguna naranja se encuentra fuera del rango indicado se la clasifica para
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
reparto. Simular el peso de cada unidad generando un número entero al azar entre
150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cosecha,
 considerando que la ocupación del camión no debe ser inferior al 80%; en
caso contrario el camión no serán despachado por su alto costo. """

import random as rn

# FUNCIÓN generar_peso_naranja:
def generar_peso_naranja() -> int:
    """Genera un peso de naranja aleatorio entre 150 y 350 gramos."""
    return rn.randint(150, 350)


# FUNCIÓN contar_naranjas:
def contar_naranjas(cantidad_naranjas: int) -> tuple:
    """
    Cuenta cuántos cajones se llenan, cuántas naranjas son para jugo y si hay sobrantes.

    CONTRATO:
    PRE: "cantidad_naranjas" es un entero positivo.
    POST: Retorna una tupla con:
        - cajones_llenos: Número de cajones llenos.
        - naranjas_para_jugo: Número de naranjas para jugo.
        - sobrantes: Número de naranjas sobrantes.
        - peso_total_cajones: Peso total de los cajones llenos en gramos.
    """
    cajon_capacidad = 100
    peso_minimo = 200
    peso_maximo = 300

    cajones_llenos = 0
    naranjas_para_jugo = 0
    peso_total_cajones = 0

    while cantidad_naranjas > 0:
        naranjas_actuales = min(cantidad_naranjas, cajon_capacidad)
        peso_cajon = 0
        for _ in range(naranjas_actuales):
            peso = generar_peso_naranja()
            if peso < peso_minimo or peso > peso_maximo:
                naranjas_para_jugo += 1
            else:
                peso_cajon += peso
        cantidad_naranjas -= cajon_capacidad
        peso_total_cajones += peso_cajon
        cajones_llenos += 1

    sobrantes = cantidad_naranjas % cajon_capacidad
    return cajones_llenos, naranjas_para_jugo, sobrantes, peso_total_cajones


# FUNCIÓN calcular_peso_total:
def calcular_peso_total(cajones_llenos: int, peso_por_cajon: int) -> int:
    """Calcula el peso total basado en el número de cajones y el peso por cajón.

    CONTRATO:
    PRE: "cajones_llenos" (int) es el número de cajones llenos.
         "peso_por_cajon (int) es el peso total del contenido de un cajón.
    POST: Retorna el peso total (int) calculado como cajones_llenos * peso_por_cajon.
    """
    return cajones_llenos * peso_por_cajon


# FUNCIÓN calcular_camiones_necesarios:
def calcular_camiones_necesarios(peso_total: int, capacidad_camion: int) -> int:
    """Calcula la cantidad de camiones necesarios sin considerar la ocupación mínima.

    CONTRATO:
    PRE: peso_total" (int) es el peso total de la carga a transportar.
         capacidad_camion (int) es la capacidad de carga de un camión.
    POST: Retorna el número de camiones necesarios (int), redondeado hacia arriba.
    """
    return -(-peso_total // capacidad_camion)  # Redondeo hacia arriba


# FUNCIÓN ajustar_camiones:
def ajustar_camiones(
    camiones_necesarios: int,
    peso_total: int,
    capacidad_camion: int,
    ocupacion_minima: float,
) -> int:
    """Ajusta el número de camiones considerando la ocupación mínima del 80%.

    CONTRATO:
    PRE: "camiones_necesarios" (int) es el número de camiones calculado sin ajuste.
         "peso_total" (int) es el peso total de la carga.
         "capacidad_camion" (int) es la capacidad de carga de un camión.
         "ocupacion_minima" (float) es el porcentaje mínimo de ocupación requerido para el último camión.
    POST: Retorna el número ajustado de camiones necesarios (int), con un mínimo de 1.
    """
    peso_efectivo = camiones_necesarios * capacidad_camion
    peso_minimo_requerido = capacidad_camion * ocupacion_minima
    if peso_efectivo - peso_total < peso_minimo_requerido:
        camiones_necesarios -= 1
    return max(camiones_necesarios, 1)


# FUNCIÓN determinar_camiones:
def determinar_camiones(cajones_llenos: int, peso_por_cajon: int) -> str:
    """Determina el número de camiones necesarios o indica si no se requiere camión.

    CONTRATO:
    PRE: "cajones_llenos" (int) es el número de cajones llenos.
         "peso_por_cajon" (int) es el peso total del contenido de un cajón.
    POST: Retorna un mensaje (str) indicando la cantidad de camiones necesarios o que no se necesita camión.
    """
    capacidad_camion = 500
    ocupacion_minima = 0.80

    peso_total = calcular_peso_total(cajones_llenos, peso_por_cajon)

    if peso_total == 0:
        return "No se necesita el camión"

    camiones_necesarios = calcular_camiones_necesarios(peso_total, capacidad_camion)
    camiones_ajustados = ajustar_camiones(
        camiones_necesarios, peso_total, capacidad_camion, ocupacion_minima
    )

    return str(camiones_ajustados)


# FUNCIÓN main:
def main() -> None:
    """Muestra la cantidad de cajones llenos, naranjas para jugo, sobrantes y camiones necesarios.

    CONTRATO:
    PRE: El usuario ingresa un número entero positivo que representa la cantidad de naranjas cosechadas.
    POST: La función muestra en pantalla:
         Cajones llenos: El número de cajones que se han llenado con naranjas.
         Naranjas para jugo: El número de naranjas que no cumplen con el rango de peso para ser clasificadas como jugo.
         Sobrantes de naranjas: El número de naranjas que quedan después de llenar los cajones.
         Camiones necesarios: La cantidad de camiones necesarios para transportar el peso total de los cajones llenos.
         No tiene parametros de retorno.
    """
    cantidad_naranjas = int(input("Ingrese la cantidad de naranjas cosechadas: "))

    cajon_capacidad = 100
    peso_por_cajon = 25000  # Peso promedio de un cajón (asumiendo 100 naranjas a 250 gramos cada una)

    cajones_llenos, naranjas_para_jugo, sobrantes, peso_total_cajones = contar_naranjas(
        cantidad_naranjas
    )
    camiones_necesarios = determinar_camiones(cajones_llenos, peso_por_cajon)

    print(f"Cajones llenos: {cajones_llenos}")
    print(f"Naranjas para jugo: {naranjas_para_jugo}")
    print(f"Sobrantes de naranjas: {sobrantes}")
    print(f"Camiones necesarios: {camiones_necesarios}")


if __name__ == "__main__":
    main()
