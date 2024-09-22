""" Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
que no sean múltiplos de 5. A y B se ingresar desde el teclado. """


# FUNCIÓN: ingreso_num
def ingreso_num() -> tuple[int, int]:
    """
    CONTRATO:
    PRE:
    No hay condiciones específicas de entrada.
    EL usuario debe ingresar un valor "a" y un valor "b" ambos valores deben de ser enteros.
    POST:
    Retorna una tupla (a, b) con los valores ingresados por el usuario.
    """

    a = int(input("Introduce el valor de A: "))
    b = int(input("Introduce el valor de B: "))
    return (a, b)


# FUNCIÓN: main
def main() -> None:
    """
    CONTRATO:
     PRE:
        Los valores A y B se ingresan desde el teclado.
     POST:
        Imprime la lista de múltiplos de 7 que no sean múltiplos de 5 en el rango [A, B].
        No tiene  parametros de retorno.
    """
    # Leer los valores de A y B
    a, b = ingreso_num()
    if a > b:
        print(f"EL número A : {a} tiene qeue ser menor o igual que B:  {b}\n ")
        print("ingrese valores validos")

    # Generar la lista de múltiplos de 7 que no sean múltiplos de 5 en el rango [A, B]
    multiples = [num for num in range(a, b + 1) if num % 7 == 0 and num % 5 != 0]
    print(multiples)


if __name__ == "__main__":
    main()
