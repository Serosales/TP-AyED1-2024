""" Desarrollar una función que reciba como parámetros dos números enteros positivos
y devuelva como valor de retorno el número que resulte de concatenar ambos
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567.
 No se permite utilizar facilidades de Python no vistas en clase."""


# Función que concatena dos números enteros
def concatenar(num1: int, num2: int) -> int:
    """Concatenar dos números enteros positivos.

    PRE:
      num1 y num2 son enteros positivos.
    POST:
      Devuelve un número entero resultante de la concatenación de num1 y num2.
    """
    # Usar una función lambda para concatenar y convertir a entero
    concatenar_lambda = lambda n1, n2: int(str(n1) + str(n2))
    return concatenar_lambda(num1, num2)


# Función que pide al usuario dos números enteros
def numeros() -> tuple[int, int]:
    """CONTRATO:
    PRE:
      Se debe ingresar por teclado dos números(positivos) positos.
    POST:
       Devuelve una tupla con los dos números ingresados."""
    
    primer_numero = int(input("Ingrese el primer número: "))
    segundo_numero = int(input("Ingrese el segundo número: "))

    return (primer_numero, segundo_numero)


# Función principal
def main() -> None:
    """CONTRATO:
    PRE:
      Función principal que ejecuta el programa.
    POST:
      Imprime el resultado concatenado de los dos números.
      No tiene parametros de retorno."""
    a, b = numeros()  # Obtener los números del usuario
    resultado = concatenar(a, b)  # Concatenar los números
    print(f"Resultado de la concatenación: {resultado}")


# Ejecutar el programa
if __name__ == "__main__":
    main()
