# Trabajo Práctico 5: Manejo de excepciones

""" . Escribir un programa que juegue con el usuario a adivinar un número. El programa
debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar
el número. Si el usuario introduce algo que no sea un número se mostrará un
mensaje en pantalla y se lo contará como un intento más."""

from random import randint as rn

# FUNCIÓN: iniciar_juego
def iniciar_juego() -> None:
    """
    Inicia el juego de adivinar el número y controla el flujo del juego.
    
    PRE: Ninguno.
    POST: No retorna nada. Inicia el juego y muestra el número de intentos.
    """
    numero_oculto = rn(1, 500)
    intentos_usuario = []

    print("¡Bienvenido al juego de adivinar el número!")
    print("He elegido un número entre 1 y 500. ¡Intenta adivinarlo!")

    while True:
        intento_usuario = input("Ingrese su adivinanza: ")
        intentos_usuario.append(intento_usuario)  # Agrega el intento al contador

        try:
            adivinanza = int(intento_usuario)

            if adivinanza < 1 or adivinanza > 500:
                print("Por favor, ingrese un número entre 1 y 500.")
                continue
            
            if adivinanza < numero_oculto:
                print("El número a adivinar es mayor.")
            elif adivinanza > numero_oculto:
                print("El número a adivinar es menor.")
            else:
                cantidad_intentos = len(intentos_usuario) 
                print(f"¡Felicidades! Adivinaste el número {numero_oculto} en {cantidad_intentos} intentos.")
                break
        
        except ValueError:
            print("Error: Debe ingresar un número válido.")
            # No se incrementa intentos si no es un número

# FUNCIÓN: principal
def main() -> None:
    """
    Función principal que ejecuta el flujo del juego.
    
    PRE: Ninguno.
    POST: No retorna nada. Llama a la función iniciar_juego para comenzar el juego.
    """
    iniciar_juego()

if __name__ == "__main__":
    main()
