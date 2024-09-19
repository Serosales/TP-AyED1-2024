"""1. Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita
verificar su funcionamiento.
"""
# FUNCIÓN: es_capicua
def es_capicua(cadena: str) -> bool:
    """
    CONTRATO:
     PRE: 
       La cadena debe ser una secuencia de caracteres (string).
     POST: 
       Retorna True si la cadena es capicúa, False en caso contrario."""
    
    # Inicializamos los índices para comparar caracteres
    inicio = 0
    fin = len(cadena) - 1
    
    # Comparamos los caracteres desde los extremos hacia el centro
    while inicio < fin:
        if cadena[inicio] != cadena[fin]:
            return False  # No es capicúa
        inicio += 1
        fin -= 1
    
    return True  # Es capicúa

# FUNCIÓN: main
def main() -> None:
    """
    CONTRATO:
     PRE: 
       No hay requisitos previos.
     POST: 
       Solicita una cadena al usuario y muestra si es capicúa.
       No tiene parametro de retorno."""
    
    cadena = input("Ingrese una cadena de caracteres: ")
    
    # Usando un diccionario para almacenar el resultado
    resultados = {
        'es_capicua': es_capicua(cadena)
    }
    
    # Imprimir el resultado usando una función lambda
    imprimir_resultado = lambda res: print("La cadena es capicúa." if res else "La cadena no es capicúa.")
    
    imprimir_resultado(resultados['es_capicua'])

# Ejecutar el programa
if __name__ == "__main__":
    main()

