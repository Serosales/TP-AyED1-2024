""". Desarrollar una función para reemplazar todas las apariciones de una palabra por
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la
cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse
palabras completas, y no fragmentos de palabras. Escribir también un programa
para verificar el comportamiento de la función. """

import re
from typing import Tuple, Dict

def obtener_mensajes_ingreso() -> Tuple[str, str, str]:
    """
    Obtiene los mensajes de ingreso del usuario.

    PRE: 
    Ninguno.

    POST:
    Devuelve una tupla que contiene tres cadenas: el texto de entrada, la palabra original y la nueva palabra.
    Las cadenas devueltas no están vacías.
    """
    mensaje_ingreso_texto = "Ingrese el texto: "
    mensaje_ingreso_palabra_original = "Ingrese la palabra a reemplazar: "
    mensaje_ingreso_palabra_nueva = "Ingrese la nueva palabra: "
    return (mensaje_ingreso_texto, mensaje_ingreso_palabra_original, mensaje_ingreso_palabra_nueva)

def obtener_palabra(mensaje:str)->str:
    """
    Obtiene una palabra del usuario.

    PRE:
    mensaje es una cadena no vacía.
    El usuario ingresará una cadena no vacía cuando se le pida.

    POST:
    Devuelve una cadena única ingresada por el usuario.
    La cadena devuelta no está vacía.
    """
    return [palabra for palabra in iter(lambda: input(mensaje), '') if palabra.strip()][0]

def reemplazar_palabra(texto: str, palabra_original: str, palabra_nueva: str) -> Tuple[str, int]:
    """
    Reemplaza la palabra original por la palabra nueva en el texto.

    PRE:
    texto es una cadena no vacía.
    palabra_original es una cadena no vacía.
    palabra_nueva es una cadena no vacía.
    palabra_original existe en texto.

    POST:
    Devuelve una tupla que contiene el texto modificado y la cantidad de reemplazos realizados.
    El texto modificado tiene todas las ocurrencias de palabra_original reemplazadas por palabra_nueva.
    La cantidad de reemplazos realizados es precisa.
    """
    patron = r'\b' + re.escape(palabra_original) + r'\b'
    cantidad_reemplazos = sum(1 for _ in re.finditer(patron, texto))
    texto_reemplazado = re.sub(patron, palabra_nueva, texto)
    return texto_reemplazado, cantidad_reemplazos

def mostrar_resultados(resultados) -> str:
    """
    Muestra los resultados en la consola.

    PRE:
    resultados es un diccionario con claves y valores de cadena.
    El diccionario contiene las claves esperadas: "Texto original", "Texto modificado", y "Cantidad de reemplazos realizados".

    POST:
    Imprime los resultados en la consola en un formato legible.
    Retorna una cadena con los resultados impresos.
    """
    salida = "\nResultados:\n"
    for clave, valor in resultados.items():
        salida += f"{clave}:\n{valor}\n" + "-" * 50 + "\n"
    print(salida)
    return salida

def ejecutar_programa() -> Dict[str, str]:
    """
    Ejecuta el programa principal.

    POST:
    Retorna un diccionario con los resultados del procesamiento de texto.
    """
    mensaje_ingreso_texto, mensaje_ingreso_palabra_original, mensaje_ingreso_palabra_nueva = obtener_mensajes_ingreso()
    texto = obtener_palabra(mensaje_ingreso_texto)
    palabra_original = obtener_palabra(mensaje_ingreso_palabra_original)
    palabra_nueva = obtener_palabra(mensaje_ingreso_palabra_nueva)
    texto_reemplazado, cantidad_reemplazos = reemplazar_palabra(texto, palabra_original, palabra_nueva)
    
    resultados = {
        "Texto original": texto,
        "Texto modificado": texto_reemplazado,
        "Cantidad de reemplazos realizados": cantidad_reemplazos
    }
    
    mostrar_resultados(resultados)
    return resultados

def main() -> None:
    """
    Punto de entrada del programa.

    POST:
    Ejecuta el programa principal, coordinando la obtención de datos del usuario y mostrando resultados.
    """
    ejecutar_programa()

if __name__ == "__main__":
    main()

