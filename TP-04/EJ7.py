"""7. Escribir una función para eliminar una subcadena de una cadena de caracteres, a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""
# FUNCIÓN: Eliminar subcadena utilizando rebanadas
def eliminar_con_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    CONTRATO:
    Elimina una subcadena de la cadena original desde la posición especificada
    hasta la posición + cantidad.

    PRE:
      "cadena" debe ser no vacía.
      "posicion" debe ser mayor o igual  0 y menor que la  longitud de cadena.
      "cantidad" debe ser mayor o igual  0.

    POST:
     Devuelve la cadena resultante después de la eliminación.
    """
    if cantidad > 0:  # Si la cantidad es positiva
        return cadena[:posicion] + cadena[posicion + cantidad:]
    return cadena

# FUNCIÓN: Eliminar subcadena sin utilizar rebanadas
def eliminar_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    CONTRATO:
    Elimina una subcadena de la cadena original desde la posición especificada
    hasta la posición + cantidad sin utilizar rebanadas.

    PRE:
      "cadena" debe ser no vacía.
      "posicion" debe ser mayor o igual  0 y menor que la  longitud de cadena.
      "cantidad" debe ser mayor o igual  0.

    POST:
     Devuelve la cadena resultante después de la eliminación.
     Si la cadena es de valor 0 devuelve la cadena original.
    """
    if cantidad > 0:  # Si la cantidad es positiva
        salida = ''
        for i in range(len(cadena)):
            if i < posicion or i >= (posicion + cantidad):
                salida += cadena[i]
        return salida
    return cadena

def main():
    """
    Función principal que imprime los resultados de la eliminación de subcadenas
    para verificar su correcto funcionamiento.
    """
    cadena_1 = "Cadena de caracteres !"
    posicion_1 = 5
    cantidad_1 = 7

    resultado_rebanadas = eliminar_con_rebanadas(cadena_1, posicion_1, cantidad_1)
    print(f"Resultado con rebanadas: '{resultado_rebanadas}'")
    
    resultado_sin_rebanadas = eliminar_sin_rebanadas(cadena_1, posicion_1, cantidad_1)
    print(f"Resultado sin rebanadas: '{resultado_sin_rebanadas}'")

if __name__ == "__main__":
    main()
