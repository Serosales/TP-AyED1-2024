"""1. Desarrollar una función que reciba tres números enteros positivos y devuelva el
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y mostrar
el máximo hallado, o un mensaje informativo si éste no existe"""

def encontrar_numero_mayor(num_1: int, num_2: int, num_3: int) -> int:
    """
    Pre:
        Devuelve el mayor de los tres números solo si es único.
    Post:
        1Devuelve -1 si no hay un número máximo único. 
    """
    # Encontrar el mayor de los tres números.
    numero_maximo = max(num_1, num_2, num_3)
    
    # Verificar si el número máximo es único
    conteo_maximo = (numero_maximo == num_1) + (numero_maximo == num_2) + (numero_maximo == num_3)
    
    if conteo_maximo == 1:
        return numero_maximo
    else:
        return -1

def ingrese_los_numeros() -> tuple:
    """
    Pre:
        Solicita al usuario ingresar tres números enteros positivos.

    Post:
        Devuelve una tupla con los tres números ingresados.
    """
    primer_numero = int(input("Ingrese el primer número: "))
    segundo_numero = int(input("Ingrese el segundo número: "))
    tercer_numero = int(input("Ingrese el tercer número: "))

    return (primer_numero, segundo_numero, tercer_numero)

def verificar_resultado(resultado: int) -> str:
    
    """
     Pre:
        "resultado" es un número entero. Puede ser un número positivo o -1.
    Post:
         Si "resultado" es -1, la función retorna el mensaje "NO SE PUDO ENCONTRAR UN ÚNICO NÚMERO MÁXIMO".
         de lo contrario , la función retorna un mensaje en la forma "EL NÚMERO MÁXIMO ÚNICO ES ", resultado.
    """

    if resultado == -1:
        return "NO SE PUDO ENCONTRAR UN ÚNICO NÚMERO MÁXIMO"
    else:
        return f"EL NÚMERO MÁXIMO ÚNICO ES {resultado}"

if __name__ == "__main__":
    # Invocación de las funciones
    primer_numero, segundo_numero, tercer_numero = ingrese_los_numeros()
    resultado_maximo = encontrar_numero_mayor(primer_numero, segundo_numero, tercer_numero)
    mensaje = verificar_resultado(resultado_maximo)
    print(mensaje)