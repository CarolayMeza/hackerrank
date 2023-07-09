"""
Inicializa las variables minSum y maxSum con el valor máximo posible de un entero (MAX_INT).
Itera a través de cada elemento de la matriz.
Para cada elemento, calcula la suma de todos los elementos en la matriz excepto el elemento actual.
Actualiza minSum y maxSum comparando la suma calculada con las sumas mínima y máxima actuales.
Después de la iteración, imprime los valores de minSum y maxSum."""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
# Lee la matriz de entrada que contiene cinco números enteros.
def miniMaxSum(arr):
    minSum = float('inf')  # Inicializar la suma mínima con un valor infinito
    maxSum = float('-inf')  # Inicializar la suma máxima con un valor menos infinito

    for i in range(len(arr)):
        totalSum = sum(arr) - arr[i]  # Calcular la suma total excluyendo el elemento actual
        minSum = min(minSum, totalSum)  # Actualizar la suma mínima si la suma actual es menor
        maxSum = max(maxSum, totalSum)  # Actualizar la suma máxima si la suma actual es mayor

    print(minSum, maxSum)

# Leer la entrada
arr = list(map(int, input().split()))

# Llamar a la función con la matriz de entrada
miniMaxSum(arr)


