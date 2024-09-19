"""Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la
misma tiene 80 columnas."""

"""Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la misma tiene 80 columnas."""

# FUNCIÓN: Centrar una cadena de caracteres en una pantalla de 80 columnas
def centrar_cadena(cadena):
    """
    CONTRATO:
    PRE: 
        La longitud de la cadena es menor o igual a 80
    POST: 
        Se devuelve la cadena centrada en una longitud de 80 caracteres
    """
    longitud = len(cadena)
    espacios = (80 - longitud) // 2
    return ' ' * espacios + cadena

# FUNCIÓN: Leer una cadena de caracteres e imprimirla centrada
def main():
    """ 
    CONTRATO:
    PRE: 
        Se espera una cadena de entrada del usuario
    POST: 
        Se imprime la cadena centrada en la pantalla
    """
    cadena = input("Introduce una cadena de caracteres: ")
    
    # Usamos rebanadas para limitar la longitud a 80 caracteres (en caso de ser necesario)
    cadena = cadena[:80]
    
    # Generar la cadena centrada
    cadena_centrada = centrar_cadena(cadena)
    
    # Imprimir la cadena centrada
    print(cadena_centrada)

if __name__ == "__main__":
    main()
