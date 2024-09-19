""" . Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.
b. Calcular y devolver el producto de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar
listas auxiliares.
d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50]"""

import random as rn
rn.seed(100)

# FUNCION: generar_lista_aleatoria
def generar_lista_aleatoria() -> list:
    """
    Genera una lista con números aleatorios de cuatro dígitos.
    PRE: Ninguna.
    POST: Devuelve una lista de enteros, donde cada entero es un número aleatorio de cuatro dígitos (entre 1000 y 9999). La longitud de la lista es un número aleatorio de dos dígitos (entre 10 y 99).
    """
    cantidad_elementos = rn.randint(10, 99)  # Número aleatorio de 2 dígitos
    lista = [rn.randint(1000, 9999) for _ in range(cantidad_elementos)]
    return lista


# FUNCION: producto_lista
def producto_lista(lista: list) -> int:
    """
    Calcula y devuelve el producto de todos los elementos de la lista.
    PRE: lista es una lista de enteros no vacía.
    POST: Devuelve un entero que es el producto de todos los elementos en la lista.
    """
    producto = 1
    for num in lista:
        producto *= num
    return producto


# FUNCION: eliminar_valor
def eliminar_valor(lista: list, valor: int) -> None:
    """
    Elimina todas las apariciones de un valor en la lista sin usar listas auxiliares.
    PRE: lista es una lista de enteros. valor es un entero que puede o no estar en lista.
    POST: Modifica lista para eliminar todas las ocurrencias de valor. No retorna ningún valor.
    """
    while valor in lista:
        lista.remove(valor)


# FUNCION: es_capicua
def es_capicua(lista: list) -> bool:
    """
    Determina si el contenido de una lista es capicúa sin usar listas auxiliares.
    PRE: lista es una lista de enteros.
    POST: Devuelve True si lista es capicúa (es decir, si es igual a sí misma al revés), y False en caso contrario.
    """
    n = len(lista)
    for i in range(n // 2):
        if lista[i] != lista[n - 1 - i]:
            return False
    return True


# FUNCION: main
def main() -> None:
    """
    Función principal que ejecuta el programa.
    PRE: Ninguna.
    POST: Ejecuta el programa, generando una lista aleatoria, calculando su producto, eliminando un valor especificado y
      determinando si la lista es capicúa. Imprime los resultados.
    """
    # a. Cargar una lista con números al azar de cuatro dígitos
    lista = generar_lista_aleatoria()
    print("Lista generada:", lista)

    # b. Calcular y devolver el producto de todos los elementos de la lista
    producto = producto_lista(lista)
    print("Producto de los elementos de la lista:", producto)

    # c. Eliminar todas las apariciones de un valor en la lista
    valor_a_eliminar = int(input("Ingrese el valor a eliminar de la lista: "))
    eliminar_valor(lista, valor_a_eliminar)
    print("Lista después de eliminar el valor", valor_a_eliminar, ":", lista)

    # d. Determinar si la lista es capicúa
    es_capicua_lista = es_capicua(lista)
    print("La lista es capicúa:", es_capicua_lista)


if __name__ == "__main__":
    main()
