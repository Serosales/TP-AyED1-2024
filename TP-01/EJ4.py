"""4. Un comercio de electrodomésticos necesita para su línea de cajas un programa que
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados como vuelto,
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1
billete de $200, 1 billete de $100 y 3 billetes de $10."""


# FUNCIÓN: calcular_cambio
def calcular_cambio(total_compra: int, dinero_recibido: int) -> list:
    """
    CONTRATO:
    PRE:
        total_compra >= 0, dinero_recibido >= 0
    POST:
        Devuelve una lista con la cantidad de billetes a devolver como cambio,
        o un mensaje de error si no es posible dar el cambio.
    """
    # Definimos las denominaciones de los billetes disponibles
    billetes = [5000, 1000, 500, 200, 100, 50, 10]

    # Verificamos si el dinero recibido es suficiente
    if dinero_recibido < total_compra:
        return ["Error: Dinero recibido insuficiente."]

    # Calculamos el cambio
    cambio = dinero_recibido - total_compra

    # Lista para almacenar la cantidad de cada billete
    cantidades = []

    # Recorremos las denominaciones de los billetes
    for billete in billetes:
        if cambio >= billete:
            cantidad = cambio // billete  # Cantidad de billetes de esta denominación
            cantidades.append(
                (billete, cantidad)
            )  # Agregamos la tupla (billete, cantidad)
            cambio -= cantidad * billete  # Reducimos el cambio restante

    # Verificamos si se ha podido entregar el cambio completo
    if cambio > 0:
        return [
            "Error: No se puede entregar el cambio con las denominaciones disponibles."
        ]

    return cantidades


# FUNCIÓN: solicitar_datos
def solicitar_datos() -> tuple:
    """
    CONTRATO:
    PRE:
        No hay requisitos específicos para la entrada del usuario.
    POST:
        Devuelve una tupla con el total de la compra y el dinero recibido.
    """
    total_compra = int(input("Ingrese el total de la compra: "))
    dinero_recibido = int(input("Ingrese el dinero recibido: "))
    return (total_compra, dinero_recibido)


# FUNCIÓN: main
def main():
    """
    CONTRATO:
    PRE:
        No hay requisitos específicos para la entrada del usuario,
        pero se asume que el usuario ingresará valores enteros válidos.
    POST:
        Solicita al usuario el total de la compra y el dinero recibido,
        calcula el cambio utilizando la función calcular_cambio,
        y muestra el resultado en la consola.
        Puede ser el cambio a entregar o un mensaje de error.
    """
    # Solicitar datos al usuario
    total_compra, dinero_recibido = solicitar_datos()

    # Calcular y mostrar el resultado
    resultado = calcular_cambio(total_compra, dinero_recibido)

    # Verificamos si el resultado es un mensaje de error
    if (
        resultado.count("Error: Dinero recibido insuficiente.") > 0
        or resultado.count(
            "Error: No se puede entregar el cambio con las denominaciones disponibles."
        )
        > 0
    ):
        print(resultado[0])  # Imprimir el mensaje de error
    else:
        print("Cambio a entregar:")
        for billete, cantidad in resultado:
            print(f"${billete}: {cantidad} billete(s)")


if __name__ == "__main__":
    main()
