""" 4. Eliminar de una lista de números enteros aquellos valores que se encuentren en
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista
resultante. La función debe modificar la lista original sin crear una copia modificada."""


# FUNCIÓN: eliminar_valores
def eliminar_valores(lista_original:list, lista_eliminar:list):
    """Elimina de lista_original aquellos valores que se encuentren en lista_eliminar.
    Modifica lista_original directamente.

    CONTRATO:
    PRE:
        lista_original debe ser una lista de números enteros.
        lista_eliminar debe ser una lista de números enteros.
        Ambos parámetros deben ser listas (no None y no deben ser de otro tipo).

    POST:
        Todos los elementos de lista_eliminar que están presentes en lista_original deben ser eliminados de lista_original.
        lista_original debe ser modificada directamente, y su longitud puede ser menor o igual a la longitud original.
        La función no retorna ningún valor.
    """
    i = 0
    while i < len(lista_original):
        if lista_original[i] in lista_eliminar:
            lista_original.pop(i)
        else:
            i += 1
            
# FUNCIÓN: main
def main()->None:
    """Solicita al usuario dos listas de enteros, imprime las listas antes y después de eliminar los valores de la lista original.
    
    CONTRATO:
    PRE:
        El usuario debe ingresar dos listas de enteros separadas por espacios cuando se le solicite.
        Las entradas deben ser válidas para convertir a listas de enteros (es decir, deben ser números enteros).

    POST:
        Imprime lista_original antes de realizar las eliminaciones.
        Imprime lista_eliminar.
        Imprime lista_original después de realizar las eliminaciones, mostrando la lista resultante después de aplicar eliminar_valores.

    """
    # Solicitar la lista original
    lista_original = list(map(int, input("Ingrese la lista original (separada por espacios): ").split()))
    
    # Solicitar la lista de valores a eliminar
    lista_eliminar = list(map(int, input("Ingrese la lista de valores a eliminar (separada por espacios): ").split()))
    
    # Mostrar las listas antes de la eliminación
    print("Lista original:", lista_original)
    print("Lista de valores a eliminar:", lista_eliminar)
    
    # Eliminar los valores
    eliminar_valores(lista_original, lista_eliminar)
    
    # Mostrar la lista resultante
    print("Lista resultante después de eliminar los valores:", lista_original)

if __name__ == "__main__":
    main()
