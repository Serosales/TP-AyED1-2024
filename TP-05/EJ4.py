# Trabajo Práctico 5: Manejo de excepciones

""" Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
un programa para imprimir los números enteros entre 1 y 100000, y que solicite
confirmación al usuario antes de detenerse cuando se presione Ctrl-C.
"""
# FUNCIÓN: imprimir_numeros
def imprimir_numeros() -> None:
    """
    Imprime números del 1 al 100000.
    
    PRE: Ninguno.
    POST: Imprime un mensaje indicando si se completó la impresión o se detuvo manualmente.
    """
    print("Presione Ctrl+C para detener la ejecución.")
    try:
        for i in range(1, 100001):
            print(i)
        print("La impresión se completó.")
    except KeyboardInterrupt:
        respuesta = input("\n Ingrese 's' para detener el programa : ").strip()
        if respuesta == 's':
            print("El programa se detuvo por solicitud del usuario.")
        else:
            print("Continuando con la impresión...")
            imprimir_numeros()

if __name__ == "__main__":
    imprimir_numeros()

