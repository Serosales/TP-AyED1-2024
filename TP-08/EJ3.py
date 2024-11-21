# Trabajo Práctico 8: Tuplas, conjuntos y diccionarios

"""Desarrollar un programa que utilice una función que reciba como parámetro una
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
una tupla con las distintas partes que componen dicha dirección. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
formatos de fecha inválidos y devolver una tupla vacía. """


def descomponer_correo(correo_electronico: str) -> tuple:
    """
    Descompone una dirección de correo electrónico en sus partes: usuario, dominio,
    subdominio y extensión.

    Pre:
    correo_electronico es una cadena de texto que representa una dirección de correo electrónico.

    Post:
    Retorna una tupla con las partes del correo (usuario, dominio, subdominio, extensión),
    o una tupla vacía si el correo es inválido.
    """
    # Verificar si el correo contiene exactamente un '@' y al menos un '.'
    if correo_electronico.count("@") != 1 or correo_electronico.count(".") < 1:
        return ()

    # Dividir la dirección de correo en usuario y dominio
    usuario_correo, dominio_completo = correo_electronico.split("@", 1)

    # Dividir el dominio completo en partes (dominio, subdominio y extensión)
    partes_dominio = dominio_completo.split(".")

    # Verificar que haya al menos dos partes en el dominio (dominio y extensión)
    if len(partes_dominio) < 2:
        return ()

    # La extensión debe ser una cadena alfabética de al menos 2 caracteres
    extension_dominio = partes_dominio[-1]
    if not extension_dominio.isalpha() or len(extension_dominio) < 2:
        return ()

    # Si el dominio tiene más de una parte, se asume que la primera es el dominio
    # y el resto son subdominios (puede ser vacío si no hay subdominio)
    dominio_principal = partes_dominio[0]
    subdominio_extra = ".".join(partes_dominio[1:-1]) if len(partes_dominio) > 2 else ""

    # Retornar las partes descompuestas
    return (usuario_correo, dominio_principal, subdominio_extra, extension_dominio)


def main() -> None:
    """
    Función principal que solicita al usuario una dirección de correo electrónico
    y muestra sus partes descompuestas.

    Pre:
    El usuario debe ingresar una dirección de correo electrónico válida o inválida.
    El correo debe estar en formato de texto (cadena de caracteres).

    Post:
    Si el correo es válido, muestra las partes descompuestas (usuario, dominio, subdominio, extensión).
    Si el correo es inválido, muestra un mensaje de error indicando que la dirección no es válida.
    """
    # Solicitar la dirección de correo electrónico al usuario
    correo_electronico = input("Ingrese una dirección de correo electrónico: ")

    # Descomponer el correo y obtener las partes
    partes_del_correo = descomponer_correo(correo_electronico)

    # Si las partes no están vacías, es un correo válido
    if partes_del_correo:
        print(f"Las partes del correo '{correo_electronico}' son: {partes_del_correo}")
    else:
        print(f"La dirección de correo '{correo_electronico}' es inválida.")


if __name__ == "__main__":
    main()
