"""Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga. Se solicita:

a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe
aparecer una sola vez en el informe.

b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus
ingresos. Mostrar los registros de entrada al club antes y después de
eliminarlo. Informar cuántos ingresos se eliminaron."""

# FUNCIÓN: INGRESAR SOCIOS
def ingresar_socios() -> list[int]:
    """
    CONTRATO:
    PRE: 
        Ninguno.
    POST: 
        Retorna una lista de números de socio registrados hasta ingresar un 0.
    """
    registros = []
    while True:
        numero_socio = int(input("Ingrese el número de socio (cinco dígitos, 0 para finalizar): "))
        if numero_socio == 0:
            break
        registros.append(numero_socio)
    return registros

# FUNCIÓN: CONTAR INGRESOS
def contar_ingresos(registros: list[int]) -> dict:
    """
    CONTRATO
    PRE: 
        registros es una lista de números de socio.
    POST:
        Muestra la cantidad de veces que cada socio ingresó al club.
    """
    conteo = {socio: registros.count(socio) for socio in set(registros)}
    
    print("\nInforme de ingresos:")
    for socio, cantidad in conteo.items():
        print(f"Socio {socio}: {cantidad} veces")
    return conteo

# FUNCIÓN: ELIMINAR SOCIO
def eliminar_socio(registros: list[int]) -> int:
    """
    CONTRATO:
    PRE: 
        registros es una lista de números de socio.
    POST: 
        Retorna la cantidad de ingresos eliminados para el socio especificado.
    """
    numero_socio = int(input("\nIngrese el número de socio a eliminar: "))
    
    # Mostrar registros antes de la eliminación
    print("Registros antes de eliminar:")
    print(registros)
    
    # Contar ingresos eliminados
    ingresos_eliminados = registros.count(numero_socio)
    
    # Eliminar todos los ingresos del socio especificado
    registros[:] = list(filter(lambda socio: socio != numero_socio, registros))
    
    # Mostrar registros después de la eliminación
    print("Registros después de eliminar:")
    print(registros)
    
    return ingresos_eliminados

# FINCIÓN: main
def main()->None:
    """
    CONTRATO:
    PRE: 
    Ninguno.
    POST: 
    Imprime los informes de ingresos de socios y la cantidad de ingresos eliminados tras eliminar un socio específico.
    
    """
    # Ingresar socios
    registros = ingresar_socios()
    
    # Contar y mostrar los ingresos por socio
    contar_ingresos(registros)
    
    # Eliminar socio y mostrar resultados
    ingresos_eliminados = eliminar_socio(registros)
    print(f"\nNúmero de ingresos eliminados: {ingresos_eliminados}")

if __name__ == "__main__":
    main()
