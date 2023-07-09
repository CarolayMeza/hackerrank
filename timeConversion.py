def timeConversion(s):
    hours, minutes, seconds = map(int, s[:-2].split(':'))  # Extraer horas, minutos y segundos del formato de tiempo
    period = s[-2:]  # Obtener el período (AM o PM)

    if period == 'AM':
        if hours == 12:
            hours = 0  # Si es AM y las horas son 12, cambiarlas a 0
    elif period == 'PM':
        if hours != 12:
            hours += 12  # Si es PM y las horas no son 12, agregar 12 a las horas

    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)  # Crear una nueva cadena en formato de 24 horas

# Leer la entrada
s = input().strip()

# Llamar a la función con el tiempo de entrada
converted_time = timeConversion(s)

# Imprimir el tiempo convertido
print(converted_time)
