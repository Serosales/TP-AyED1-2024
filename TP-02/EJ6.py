""" Escribir una función que reciba una lista de números enteros como parámetro y la
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones relativas que cada elemento tiene en la lista original. Desarrollar también
un programa que permita verificar el comportamiento de la función. Por ejemplo,
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50]."""


# FUNCIÓN: normalizar
def normalizar(lista):
    """
    Normaliza una lista de números enteros de manera que la suma de los elementos normalizados sea 1.0.

    PRE:
     Entrada: Una lista de números enteros, "lista". Puede estar vacía.
     Condiciones: La lista puede contener elementos positivos, negativos o cero.

    POST:
     Salida: Una lista de números flotantes, "lista_normalizada", donde cada elemento es el resultado de dividir el correspondiente elemento de la lista original por la suma total de los elementos de la lista original.
     Propiedades: La suma de todos los elementos en `lista_normalizada` será 1.0 (o lo más cercano posible a 1.0), y cada elemento será mayor o igual a 0 y menor o igual a 1.
    """
    # Calculamos la suma de los elementos de la lista original
    suma_total = sum(lista)

    # Normalizamos cada elemento de la lista dividiéndolo por la suma total
    # usando map y lambda para aplicar la normalización a cada elemento
    lista_normalizada = list(map(lambda x: x / suma_total, lista))

    return lista_normalizada


# FUNCIÓN: main
def main() -> None:
    """
    Ejecuta un ejemplo de uso de la función  "normalizar"  y verifica el resultado.

    CONTRATO:
    PRE:
     No se requieren entradas externas para esta función.
     El entorno de ejecución debe permitir la impresión en consola.

    POST:
     Imprime la lista original y la lista normalizada en la consola.
     Imprime la suma de los elementos normalizados en la consola.
     Emite una advertencia si la suma de los elementos normalizados no es 1.0.
    """
    # Lista de ejemplo
    lista = [1, 1, 2]

    # Normalizamos la lista
    lista_normalizada = normalizar(lista)

    # Imprimimos el resultado
    print("Lista original:", lista)
    print("Lista normalizada:", lista_normalizada)

    # Verificamos que la suma de los elementos normalizados es 1.0
    suma_normalizada = sum(lista_normalizada)
    print("Suma de los elementos normalizados:", suma_normalizada)

    # Verificación manual del POST
    if abs(suma_normalizada - 1.0) >= 1e-9:
        print("Advertencia: La suma de los elementos normalizados no es 1.0")


# Llamada a la función main si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()
