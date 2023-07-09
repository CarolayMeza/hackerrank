import statistics  # Importar el módulo statistics para realizar cálculos estadísticos

def calculate_median(array):
    median = statistics.median(array)  # Calcular la mediana del array utilizando la función median del módulo statistics
    return median

if __name__ == "__main__":
    my_array = [5, 3, 1, 2, 4]  # Crear un array de ejemplo
    result = calculate_median(my_array)  # Llamar a la función calculate_median con el array como argumento
    print("median:", result)  # Imprimir el resultado de la mediana
