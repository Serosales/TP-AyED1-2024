"""12. Escribir un programa para crear una lista por comprensión con los naipes de la baraja española.
 La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros", "2
Oros"... ]. Imprimir la lista por pantalla. """

# FUNCIÓN: crear_baraja
def crear_baraja() -> list:
    """
    CONTRATO: 
    PRE: Crea una lista de naipes de la baraja española.
    POST: Devuelve una lista de cadenas representando los naipes.
    """
    palos = ["Oros", "Copas", "Espadas", "Bastos"]
    numeros = [str(i) for i in range(1, 8)] + ["Sota", "Caballo", "Rey"]
    
    return [f"{numero} {palo}" for palo in palos for numero in numeros]

# FUNCIÓN: main
def main()->None:
    """
    CONTRATO: 
    PRE: No requiere parámetros.
    POST: Imprime la lista de naipes de la baraja española.
    No tiene parametro de retorno.
    """
    baraja = crear_baraja()
    print(baraja)

if __name__ == "__main__":
    main()
