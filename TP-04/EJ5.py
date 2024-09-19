"""5. Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo una frase y un entero N, y devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original. Escribir también un programa para
verificar el comportamiento de la misma. Hacer tres versiones de la función, para
cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter"""

# FUNCIÓN: filtrar_palabras_ciclos
# a. Utilizando sólo ciclos normales
def filtrar_palabras_ciclos(frase: str, n: int) -> str:
    """
    CONTRATO: 
    PRE: 
        Frase es una cadena de caracteres y n es un entero positivo.
    POST: 
        Devuelve una cadena de palabras que tienen al menos n caracteres.
    """
    palabras = frase.split()
    resultado = []
    for palabra in palabras:
        if len(palabra) >= n:
            resultado.append(palabra)
    return ' '.join(resultado)

# FUNCIÓN: filtrar_palabras_listas_comp
# b. Utilizando listas por comprensión
def filtrar_palabras_listas_comp(frase: str, n: int) -> str:
    """
    CONTRATO: 
    PRE: 
        Frase es una cadena de caracteres y n es un entero positivo.
    POST: 
        Devuelve una cadena de palabras que tienen al menos n caracteres.
    """
    return ' '.join([palabra for palabra in frase.split() if len(palabra) >= n])

# FUNCIÓN: filtrar_palabras_filter
def filtrar_palabras_filter(frase: str, n: int) -> str:
    """
    CONTRATO: 
    PRE: 
        Frase es una cadena de caracteres y n es un entero positivo.
    POST:  
        Devuelve una cadena de palabras que tienen al menos n caracteres.
    """
    return ' '.join(filter(lambda palabra: len(palabra) >= n, frase.split()))

# FUNCIÓN: filtrar_palabras_diccionario
def filtrar_palabras_diccionario(frase: str, n: int) -> str:
    """
    CONTRATO: 
    PRE: 
        Frase es una cadena de caracteres y n es un entero positivo.
    POST: 
        Devuelve una cadena de palabras que tienen al menos n caracteres.
    """
    palabras = frase.split()
    resultado = {palabra: len(palabra) for palabra in palabras if len(palabra) >= n}
    return ' '.join(resultado.keys())

def main():
    frase = "La programación en Python es muy divertida y educativa"
    n = 5

    print("Original:", frase)
    print("Filtrado con ciclos:", filtrar_palabras_ciclos(frase, n))
    print("Filtrado con listas por comprensión:", filtrar_palabras_listas_comp(frase, n))
    print("Filtrado con filter:", filtrar_palabras_filter(frase, n))
    print("Filtrado con diccionario:", filtrar_palabras_diccionario(frase, n))

if __name__ == "__main__":
    main()
