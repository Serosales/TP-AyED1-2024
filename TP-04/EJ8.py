"""8. Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros."""

# FUNCIÓN:
def obtener_ultimos_n_caracteres(cadena: str, N: int) -> str:
    """
    CONTRATO:
    PRE: 
        N >= 0 y N <= len(cadena), cadena es una cadena no vacía.
    POST: 
        Retorna una subcadena con los últimos N caracteres de la cadena dada.
    """
    return cadena[-N:] if N > 0 else ''

# FUNCIÓN: 
def main() -> None:
    """
    CONTRATO:
    PRE: 
        Se ingresa una cadena no vacía y un valor de N entre 0 y la longitud de la cadena.
    POST: 
        Imprime la subcadena con los últimos N caracteres de la cadena dada.
    """
    cadena = input("Ingrese una cadena: ")
    N = int(input("Ingrese el valor de N: "))
    print(f"Últimos {N} caracteres: {obtener_ultimos_n_caracteres(cadena, N)}")

if __name__ == "__main__":
    main()
