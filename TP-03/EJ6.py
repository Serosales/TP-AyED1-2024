"""6. Un hotel necesita un programa para gestionar la operación de sus habitaciones. El
hotel cuenta con 10 pisos y 6 habitaciones por piso. Por cada huésped o grupo
familiar que se aloja en el mismo se registra la siguiente información:
· DNI del cliente (número entero)
· Apellido y Nombre
· Fecha de ingreso (DDMMAAAA)
· Fecha de egreso (DDMMAAAA)
· Cantidad de ocupantes
Se solicita desarrollar un programa que utilice arreglos para realizar las siguientes
tareas:
a. Registrar el ingreso de huéspedes al hotel, hasta que se ingrese un número de
DNI igual a -1. Tener en cuenta que los números de DNI no pueden repetirse y
que la fecha de salida debe ser mayor a la de entrada. El piso y habitación son
asignados arbitrariamente, y no puede asignarse una habitación ya otorgada.
b. Finalizado el ingreso de huéspedes se solicita:
1. Mostrar el piso con mayor cantidad de habitaciones ocupadas.
2. Mostrar cuántas habitaciones vacías hay en todo el hotel.
3. Mostrar el piso con mayor cantidad de personas.
4. Mostrar cuál será la próxima habitación en desocuparse. La fecha actual se
ingresa por teclado. Mostrar todas las que correspondan.
5. Mostrar un listado de todos los huéspedes registrados en el hotel, ordenado
por apellido."""


# FUNCIÓN: Verifica si el DNI ya está registrado
def verificar_dni(dni: int, huespedes: list) -> bool:
    """CONTRATO
    PRE:
       dni debe ser un entero y huespedes debe ser una lista de diccionarios
    POST:
       Devuelve True si el DNI ya está registrado, False en caso contrario"""

    return any(h["dni"] == dni for h in huespedes)


# FUNCIÓN: Busca una habitación vacía en el hotel
def buscar_habitacion_vacia(hotel: list) -> str:
    """
    CONTRATO:
    PRE:
        hotel debe ser una lista de listas de None o diccionarios
    POST:
      Devuelve un mensaje indicando la habitación vacía o un mensaje que indica que no hay habitaciones disponibles
    """
    for piso in range(10):
        for habitacion in range(6):
            if hotel[piso][habitacion] is None:
                return f"Habitación vacía en piso {piso}, habitación {habitacion}."
    return "No hay habitaciones vacías."


# FUNCIÓN: Registra un huésped en el hotel
def registrar_huesped(
    dni: int,
    apellido_nombre: str,
    fecha_ingreso: str,
    fecha_egreso: str,
    cantidad_ocupantes: int,
    hotel: list,
    huespedes: list,
) -> None:
    """CONTRATO
    PRE:
      dni, apellido_nombre, fecha_ingreso, fecha_egreso deben ser válidos
    POST:
      Registra un huésped en el hotel"""
    if dni == -1:
        return
    if verificar_dni(dni, huespedes):
        print("El DNI ya está registrado.")
        return
    if fecha_egreso <= fecha_ingreso:
        print("La fecha de egreso debe ser mayor a la de ingreso.")
        return

    habitacion_asignada = buscar_habitacion_vacia(hotel)
    if habitacion_asignada is None:
        print("No hay habitaciones disponibles.")
        return

    piso, habitacion = habitacion_asignada
    huesped = {
        "dni": dni,
        "apellido_nombre": apellido_nombre,
        "fecha_ingreso": fecha_ingreso,
        "fecha_egreso": fecha_egreso,
        "cantidad_ocupantes": cantidad_ocupantes,
    }
    hotel[piso][habitacion] = huesped
    huespedes.append(huesped)


# FUNCIÓN: Devuelve el piso con más habitaciones ocupadas
def piso_con_mas_habitaciones_ocupadas(hotel: list) -> int:
    """ CONTRATO
    PRE: 
        hotel debe ser una lista de listas de diccionarios o None
    POST: 
        Devuelve el piso con más habitaciones ocupadas"""
    ocupadas_por_piso = [
        sum(1 for habitacion in range(6) if hotel[piso][habitacion] is not None)
        for piso in range(10)
    ]
    return ocupadas_por_piso.index(max(ocupadas_por_piso))


# FUNCIÓN: Devuelve la cantidad de habitaciones vacías en el hotel
def contar_habitaciones_vacias(hotel: list) -> int:
    """CONTRATO
     PRE: 
        hotel debe ser una lista de listas de None o diccionarios
     POST: 
        Devuelve la cantidad de habitaciones vacías en el hotel"""
    return sum(
        1
        for piso in range(10)
        for habitacion in range(6)
        if hotel[piso][habitacion] is None
    )


# FUNCIÓN: Devuelve el piso con más personas alojadas
def piso_con_mas_personas(hotel: list) -> int:
    """
    CONTRATO:
     PRE:
        hotel debe ser una lista de listas de diccionarios
     POST:
        Devuelve el piso con más personas alojadas"""
    personas_por_piso = [
        sum(
            hotel[piso][habitacion]["cantidad_ocupantes"]
            for habitacion in range(6)
            if hotel[piso][habitacion] is not None
        )
        for piso in range(10)
    ]
    return personas_por_piso.index(max(personas_por_piso))


# FUNCIÓN: Devuelve una lista de habitaciones que se desocuparán después de la fecha actual
def proxima_habitacion_en_desocuparse(fecha_actual: str, hotel: list) -> list:
    """CONTRATO
    PRE:
        fecha_actual debe ser una cadena en formato DDMMYYYY y hotel debe ser una lista de listas de diccionarios
     POST:
        Devuelve una lista de habitaciones que se desocuparán después de la fecha actual
    """
    proximas = sorted(
        [
            (piso, habitacion, huesped["fecha_egreso"])
            for piso in range(10)
            for habitacion in range(6)
            if (huesped := hotel[piso][habitacion]) is not None
            and huesped["fecha_egreso"] > fecha_actual
        ],
        key=lambda x: x[2],
    )
    return proximas


# FUNCIÓN: Devuelve un listado de huéspedes ordenado por apellido
def listado_huespedes_ordenado(huespedes: list) -> list:
    """CONTRATO:
    PRE:
       huespedes debe ser una lista de diccionarios
    POST:
      Devuelve un listado de huéspedes ordenado por apellido"""
    return sorted(huespedes, key=lambda h: h["apellido_nombre"])


# FUNCIÓN: Punto de entrada del programa
def main():
    hotel = [[None for _ in range(6)] for _ in range(10)]
    huespedes = []

    while True:
        dni = int(input("Ingrese el DNI del huésped (-1 para terminar): "))
        if dni == -1:
            break
        apellido_nombre = input("Ingrese el apellido y nombre del huésped: ")
        fecha_ingreso = input("Ingrese la fecha de ingreso (DDMMAAAA): ")
        fecha_egreso = input("Ingrese la fecha de egreso (DDMMAAAA): ")
        cantidad_ocupantes = int(input("Ingrese la cantidad de ocupantes: "))
        registrar_huesped(
            dni,
            apellido_nombre,
            fecha_ingreso,
            fecha_egreso,
            cantidad_ocupantes,
            hotel,
            huespedes,
        )

    print(
        "Piso con más habitaciones ocupadas:", piso_con_mas_habitaciones_ocupadas(hotel)
    )
    print("Habitaciones vacías en total:", contar_habitaciones_vacias(hotel))
    print("Piso con más personas:", piso_con_mas_personas(hotel))
    fecha_actual = input("Ingrese la fecha actual (DDMMAAAA): ")
    print(
        "Próximas habitaciones en desocuparse:",
        proxima_habitacion_en_desocuparse(fecha_actual, hotel),
    )
    print("Listado de huéspedes ordenado por apellido:")
    for huesped in listado_huespedes_ordenado(huespedes):
        print(huesped["apellido_nombre"])


if __name__ == "__main__":
    main()
