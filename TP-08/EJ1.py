#Trabajo Práctico 8: Tuplas, conjuntos y diccionarios

""". Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios, y luego escribir un programa que las vincule:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al día anterior. En ningún
caso la diferencia en horas puede superar las 24 horas."""


#EJERCICIO: 1
def ingresar_fecha() -> tuple:
    """Solicita y verifica que una fecha sea válida en formato dd-mm-aaaa."""
    while True:
        fecha_str = input("Ingresa una fecha (dd-mm-aaaa): ")
        try:
            # Dividimos la fecha en día, mes y año
            dia, mes, año = map(int, fecha_str.split('-'))
            # Verificamos si la fecha es válida
            if 1 <= mes <= 12 and 1 <= dia <= dias_en_mes(mes, año):
                return (dia, mes, año)
            else:
                print("Fecha inválida, por favor ingresa una fecha válida.")
        except ValueError:
            print("Formato incorrecto. Por favor usa el formato dd-mm-aaaa.")

def dias_en_mes(mes: int, año: int) -> int:
    """Devuelve la cantidad de días de un mes dado, teniendo en cuenta los años bisiestos."""
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Verificamos si el año es bisiesto para ajustar el mes de febrero
    if mes == 2 and (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
        return 29  # Año bisiesto
    return dias_por_mes[mes - 1]

def sumar_dias(fecha: tuple, n: int) -> tuple:
    """Suma N días a una fecha dada y retorna la nueva fecha."""
    dia, mes, año = fecha
    # Sumamos los días de uno en uno
    for _ in range(n):
        dia += 1
        if dia > dias_en_mes(mes, año):  # Si se pasa del último día del mes
            dia = 1
            mes += 1
            if mes > 12:  # Si se pasa del último mes (diciembre)
                mes = 1
                año += 1
    return (dia, mes, año)

def ingresar_horario() -> tuple:
    """Solicita y verifica que un horario sea válido en formato hh:mm."""
    while True:
        horario_str = input("Ingresa un horario (hh:mm): ")
        try:
            # Dividimos el horario en hora y minutos
            hora, minutos = map(int, horario_str.split(':'))
            if 0 <= hora < 24 and 0 <= minutos < 60:
                return (hora, minutos)
            else:
                print("Horario inválido, por favor ingresa un horario válido en formato hh:mm.")
        except ValueError:
            print("Formato incorrecto. Por favor usa el formato hh:mm.")

def diferencia_horarios(hora1: tuple, hora2: tuple) -> tuple:
    """Calcula la diferencia entre dos horarios en horas y minutos."""
    h1, m1 = hora1
    h2, m2 = hora2

    # Convertimos ambos horarios a minutos desde medianoche
    minutos_h1 = h1 * 60 + m1
    minutos_h2 = h2 * 60 + m2

    # Si el primer horario es menor que el segundo, se considera que es del día anterior
    if minutos_h1 < minutos_h2:
        minutos_h1 += 24 * 60  # Sumamos 24 horas a minutos_h1 para considerar el día anterior

    diferencia = minutos_h1 - minutos_h2
    return (diferencia // 60, diferencia % 60)

def main() -> None:
    """Función principal que vincula las funciones anteriores."""
    print("### Ingreso de fecha ###")
    fecha = ingresar_fecha()
    print(f"Fecha ingresada: {fecha[0]}-{fecha[1]}-{fecha[2]}")

    n = int(input("¿Cuántos días deseas sumar a la fecha? "))
    nueva_fecha = sumar_dias(fecha, n)
    print(f"Fecha resultante al sumar {n} días: {nueva_fecha[0]}-{nueva_fecha[1]}-{nueva_fecha[2]}")

    print("### Ingreso de horarios ###")
    horario1 = ingresar_horario()
    print(f"Primer horario ingresado: {horario1[0]}:{horario1[1]:02d}")

    horario2 = ingresar_horario()
    print(f"Segundo horario ingresado: {horario2[0]}:{horario2[1]:02d}")

    # Calcular la diferencia entre los dos horarios
    diferencia = diferencia_horarios(horario1, horario2)
    print(f"Diferencia entre los horarios: {diferencia[0]} horas y {diferencia[1]} minutos")

# Ejecutar el programa
if __name__ == "__main__":
    main()
