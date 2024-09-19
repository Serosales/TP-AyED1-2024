"""1. Desarrollar una función que reciba tres números enteros positivos y devuelva el
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y mostrar
el máximo hallado, o un mensaje informativo si éste no existe"""


# FUNCIÓN:encontrar_numero_mayor
def encontrar_numero_mayor(num_1: int, num_2: int, num_3: int) -> int:
    """
    CONTRATO:
    PRE:
        Devuelve el mayor de los tres números solo si es único.
    POST:
        Devuelve -1 si no hay un número máximo único.
    """
    # Encontrar el mayor de los tres números.
    numero_maximo = max(num_1, num_2, num_3)

    # Verificar si el número máximo es único
    conteo_maximo = (
        (numero_maximo == num_1) + (numero_maximo == num_2) + (numero_maximo == num_3)
    )

    if conteo_maximo == 1:
        return numero_maximo
    else:
        return -1


# FUNCIÓN: ingrese_los_numeros
def ingrese_los_numeros() -> tuple:
    """
    CONTRATO:
    PRE:
        Solicita al usuario ingresar tres números enteros positivos.

    POST:
        Devuelve una tupla con los tres números ingresados.
    """
    primer_numero = int(input("Ingrese el primer número: "))
    segundo_numero = int(input("Ingrese el segundo número: "))
    tercer_numero = int(input("Ingrese el tercer número: "))

    return (primer_numero, segundo_numero, tercer_numero)

#FUNCIÓN: verificar_resultado
def verificar_resultado(resultado: int) -> str:
    """
    CONTRATO:
     PRE:
        "resultado" es un número entero. Puede ser un número positivo o -1.
    POST:
         Si "resultado" es -1, la función retorna el mensaje "NO SE PUDO ENCONTRAR UN ÚNICO NÚMERO MÁXIMO".
         de lo contrario , la función retorna un mensaje en la forma "EL NÚMERO MÁXIMO ÚNICO ES ", resultado.
    """
    if resultado == -1:
        return "NO SE PUDO ENCONTRAR UN ÚNICO NÚMERO MÁXIMO"
    else:
        return f"EL NÚMERO MÁXIMO ÚNICO ES {resultado}"

#FUNCIÓN: ingrese_los_numeros
def ingrese_los_numeros() -> tuple:
    """
    CONTRATO:
     PRE:
        Se espera que el usuario ingrese tres números enteros.
     POST:
        Retorna una tupla con tres números enteros ingresados por el usuario.
    """
    primer_numero = int(input("Ingrese el primer número: "))
    segundo_numero = int(input("Ingrese el segundo número: "))
    tercer_numero = int(input("Ingrese el tercer número: "))

    return (primer_numero, segundo_numero, tercer_numero)

#FUNCIÓN: encontrar_numero_mayor
def encontrar_numero_mayor(
    primer_numero: int, segundo_numero: int, tercer_numero: int
) -> int:
    """
    CONTRATO:
     PRE:
        "resultado" es un número entero. Puede ser un número positivo o -1.
     POST:
         Si "resultado" es -1, la función retorna el mensaje "NO SE PUDO ENCONTRAR UN ÚNICO NÚMERO MÁXIMO".
         De lo contrario, la función retorna un mensaje en la forma "EL NÚMERO MÁXIMO ÚNICO ES {resultado}".
    """
    numeros = [primer_numero, segundo_numero, tercer_numero]
    maximo = max(numeros)
    if numeros.count(maximo) == 1:
        return maximo
    else:
        return -1  # Indica que no hay un único máximo

# FUNCIÓN: main
def main() -> None:
    """
    CONTRATO:
     PRE:
        No hay condiciones previas específicas para la ejecución de esta función.
     POST:
        Se solicita al usuario que ingrese tres números, se determina el número máximo único,
        se verifica el resultado y se imprime un mensaje correspondiente.
        No tiene parametro de retorno.
    """
    primer_numero, segundo_numero, tercer_numero = ingrese_los_numeros()
    resultado_maximo = encontrar_numero_mayor(
        primer_numero, segundo_numero, tercer_numero
    )
    mensaje = verificar_resultado(resultado_maximo)
    print(mensaje)


if __name__ == "__main__":
    main()
