# Trabajo Práctico 8: Tuplas, conjuntos y diccionarios

""". Una librería almacena su lista de precios en un diccionario. Diseñar un programa
para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un
listado con todos los elementos de la lista de precios e indicar cuál es el ítem más
costoso que venden en el comercio. """


def cargar_articulos() -> dict:
    """
    Carga los artículos y sus precios en un diccionario.

    Pre:
     El usuario ingresa los artículos y sus precios.

    Post:
    Retorna un diccionario con los artículos y sus respectivos precios.
    """
    articulos_precios = {}
    while True:
        articulo = input("Ingrese el nuevo artículo (o '0' para terminar): ").strip()
        if articulo == "0":
            break
        if not articulo:  # Verificamos que el artículo no esté vacío
            print("El nombre del artículo no puede estar vacío. Intente nuevamente.")
            continue
        if (
            articulo not in articulos_precios
        ):  # Verificamos que no se repita el artículo
            while True:
                try:
                    valor = float(input(f"Ingrese el precio para '{articulo}': "))
                    if valor > 0:
                        articulos_precios[articulo] = valor
                        break
                    else:
                        print("El precio debe ser un valor positivo.")
                except ValueError:
                    print("Por favor, ingrese un valor numérico válido para el precio.")
        else:
            print(f"El artículo '{articulo}' ya ha sido ingresado.")
    return articulos_precios


def incrementar_precios(diccionario: dict, porcentaje_incremento: float) -> dict:
    """
    Incrementa los precios de los artículos en el diccionario en un porcentaje dado.

    Pre:
     El diccionario diccionario debe contener artículos con sus precios.
     El porcentaje_incremento debe ser un número flotante.

    Post:
     Retorna un nuevo diccionario con los precios incrementados.
    """
    return {
        clave: valor * (1 + porcentaje_incremento / 100)
        for clave, valor in diccionario.items()
    }


def mostrar_precios(diccionario: dict) -> None:
    """
    Imprime el listado de artículos con sus precios.

    Pre:
     El diccionario diccionario debe contener artículos con sus precios.

    Po:
     Muestra una lista con los artículos y sus precios redondeados a dos decimales.
    """
    print("\nListado de precios actualizados:")
    print(f"{'Artículo':<20} {'Precio':>10}")
    for articulo, precio in diccionario.items():
        print(f"{articulo:<20} ${precio:10.2f}")

    # Encontramos el o los artículos más caros
    precio_maximo = max(diccionario.values())
    articulos_caros = [
        articulo for articulo, precio in diccionario.items() if precio == precio_maximo
    ]

    print(
        f"\nEl o los articulos más caros : {', '.join(articulos_caros)} con un precio de ${precio_maximo:.2f}"
    )


def main() -> None:
    """
    Función principal del programa. Permite cargar artículos, aplicar un incremento
    y mostrar los resultados.

    Pre:
    Se debe cargar al menos un artículo en el diccionario de precios.

    Post:
     Imprime la lista de precios y muestra el artículo más caro.
    """
    print("Bienvenido al sistema de gestión de artículos y precios.")

    articulos_precio = cargar_articulos()

    if not articulos_precio:
        print("No se han ingresado artículos. Saliendo del programa.")
        return

    # Incrementar los precios de los artículos en un 15%
    articulos_precio_actualizados = incrementar_precios(articulos_precio, 15)

    mostrar_precios(articulos_precio_actualizados)


if __name__ == "__main__":
    main()
