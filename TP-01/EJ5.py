"""5. Escribir funciones lambda para:
# Función lambda para verificar si un número es triangular
# Un número es triangular si puede ser expresado como la suma de los primeros k números naturales consecutivos.
# Por ejemplo, 10 es triangular porque 1 + 2 + 3 + 4 = 10.

b. Informar si un número es triangular. Un número se define como triangular si
puede expresarse como la suma de un grupo de números naturales consecutivos comenzando desde 1.
 Por ejemplo 10 es un número triangular porque se
obtiene sumando 1+2+3+4.
Ambas funciones lambda reciben como único parámetro el número a evaluar y devuelven True o False. 
No se permite utilizar ayudas externas a las mismas. """

# Funcion lamdba: Una función lambda es una pequeña función anónima.
# Una función lambda puede tomar cualquier número de argumentos, pero solo puede tener una expresión.


# Función lambda para verificar si un número es oblongo
# Un número es oblongo si puede ser expresado como el producto de dos números naturales consecutivos.
# Por ejemplo, 6 es oblongo porque 2 * 3 = 6.
oblongo = lambda num: any(num == k * (k + 1) for k in range(1, int(num**0.5) + 1))


# Función lambda para verificar si un número es triangular
# Un número es triangular si puede ser expresado como la suma de los primeros k números naturales consecutivos.
# Por ejemplo, 10 es triangular porque 1 + 2 + 3 + 4 = 10.
triangular = lambda num: any(
    num == k * (k + 1) // 2 for k in range(1, int((2 * num) ** 0.5) + 2)
)


def verificar_numeros(num: int) -> tuple:
    """
    CONTRATO:
    PRE:
      Num debe ser un número entero positivo.
    POST: Devuelve una tupla con dos strings:
          "Es oblongo." o "No es oblongo." según si num es un número oblongo.
          "Es triangular." o "No es triangular." según si num es un número triangular.
    """
    resultado_oblongo = "Es oblongo." if oblongo(num) else "No es oblongo."
    resultado_triangular = "Es triangular." if triangular(num) else "No es triangular."
    return (resultado_oblongo, resultado_triangular)


# FUNCIÓN main :


def main() -> None:
    """¿Bucle principal para solicitar un número al usuario y verificar sus propiedades
    CONTRATO:
    PRE:
      La entrada del usuario debe ser un número(entero) positivo.
    POST:
      Determinar si el número es oblongo o triangular.
      No tiene parametro de retorno."""
    while True:
        num = int(input("Ingrese un número: "))
        if num > 0:
            resultado_oblongo, resultado_triangular = verificar_numeros(num)
            print(resultado_oblongo)
            print(resultado_triangular)
            break
        else:
            print("El número debe ser positivo.")


if __name__ == "__main__":
    main()
