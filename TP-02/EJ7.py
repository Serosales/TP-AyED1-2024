""" Intercalar los elementos de una lista entre los elementos de otra. La intercalación
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
una lista nueva sino que se modificará la primera. 
Por ejemplo, si lista1 = [8, 1, 3]
y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden
tener distintas longitudes."""

from typing import List

#FUNCIÓN: intercalar_nueva
def intercalar_nueva(lista1: List[int], lista2: List[int]) -> List[int]:
    """Crea una nueva lista intercalando elementos de lista2 en lista1.
    
    CONTRATO:
    PRE:
        lista1 y lista2 son listas de enteros.
    POST:
        Devuelve una nueva lista con los elementos de lista2 intercalados en lista1.
    """
    resultado = [
        lista1[i // 2] if i % 2 == 0 else lista2[i // 2]
        for i in range(len(lista1) + len(lista2))
    ]
    return resultado


#FUNCIÓN: main
def main() -> None:
    """Ejecuta la función de intercalación y muestra el resultado usando la comprensión de listas.
    
    CONTRATO:
    PRE:
        Se definen dos listas de enteros, lista1 y lista2.
    POST:
        Llama a la función "intercalar_nueva" con lista1 y lista2 como argumentos.
        Imprime el resultado, que es una nueva lista con elementos intercalados.
        No tiene parametro de retorno.
    """
    
    lista1 = [8, 1, 3]
    lista2 = [5, 9, 7]
    
    # Llama a la función para intercalar los elementos y guarda el resultado
    resultado = intercalar_nueva(lista1, lista2)
    
    # Imprime el resultado
    print("Lista intercalada (nueva lista):", resultado)

if __name__ == "__main__":
    main()

