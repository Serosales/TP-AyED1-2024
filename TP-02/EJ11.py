""" 1. Resolver el siguiente problema, diseñando las funciones a utilizar:
Una clínica necesita un programa para atender a sus pacientes. Cada paciente que
ingresa se anuncia en la recepción indicando su número de afiliado (número entero
de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con
turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego
se solicita:

a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de
los pacientes atendidos por turno en el orden que llegaron a la clínica.

b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta
que se ingrese -1 como número de afiliado."""

from typing import List, Dict, Tuple


# FUNCIÓN: Registrar pacientes
def registrar_pacientes() -> tuple[list[int], list[int]]:
    """
    CONTRATO:
    Registra los pacientes en la clínica y retorna dos listas:
    una con los pacientes atendidos por urgencia y otra con los pacientes atendidos por turno.
    PRE:
        El usuario ingresa números de afiliado(4 digitos) y tipo de atención hasta ingresar -1.
    POST:
        Retorna dos listas: urgencias y turnos.
    """
    urgencias = []
    turnos = []

    while True:
        numero_afiliado = int(
            input("Ingrese el número de afiliado (4 dígitos, -1 para finalizar): ")
        )
        if numero_afiliado == -1:
            break
        tipo_atencion = int(
            input("Ingrese el tipo de atención (0 para urgencia, 1 para turno): ")
        )
        if tipo_atencion == 0:
            urgencias.append(numero_afiliado)
        elif tipo_atencion == 1:
            turnos.append(numero_afiliado)
        else:
            print("Tipo de atención no válido. Debe ser 0 o 1.")

    return urgencias, turnos


# FUNCIÓN: Mostrar listados
def mostrar_listados(urgencias: list[int], turnos: list[int]) -> None:
    """
    Muestra el listado de pacientes atendidos por urgencia y por turno.
    CONTRATO:
    PRE:
        Recibe dos listas: urgencias y turnos.
    POST:
        Imprime los pacientes atendidos por urgencia y por turno.
    """
    print("\nPacientes atendidos por urgencia:")
    for paciente in urgencias:
        print(paciente)

    print("\nPacientes atendidos por turno:")
    for paciente in turnos:
        print(paciente)


# FUNCIÓN: Buscar afiliado
def buscar_afiliado(
    urgencias: list[int], turnos: list[int]
) -> dict[int, tuple[int, int]]:
    """
    CONTRATO:
    Realiza la búsqueda de un número de afiliado y muestra cuántas veces fue atendido por turno y urgencia.
    Repite la búsqueda hasta que se ingrese -1 como número de afiliado.
    PRE:
        Recibe dos listas: urgencias y turnos.
    POST:
        Retorna un diccionario con el número de afiliado como clave y una tupla con las cantidades de urgencia y turno como valor.
    """
    resultados = {}

    while True:
        numero_afiliado = int(
            input("\nIngrese el número de afiliado a buscar (-1 para finalizar): ")
        )
        if numero_afiliado == -1:
            break
        cantidad_urgencia = urgencias.count(numero_afiliado)
        cantidad_turno = turnos.count(numero_afiliado)
        resultados[numero_afiliado] = (cantidad_urgencia, cantidad_turno)

    return resultados


def main() -> None:
    """
    CONTRATO:
     Ejecuta el programa para registrar pacientes, mostrar listados y buscar afiliados.
    PRE:
        Ninguno.
    POST:
        Muestra listados y resultados de la búsqueda de afiliados.
    """
    # Registrar pacientes
    urgencias, turnos = registrar_pacientes()

    # Mostrar los listados
    mostrar_listados(urgencias, turnos)

    # Buscar afiliados
    resultados = buscar_afiliado(urgencias, turnos)
    for afiliado, (cantidad_urgencia, cantidad_turno) in resultados.items():
        print(f"Afiliado {afiliado}:")
        print(f"  Cantidad de veces atendido por urgencia: {cantidad_urgencia}")
        print(f"  Cantidad de veces atendido por turno: {cantidad_turno}")


if __name__ == "__main__":
    main()
