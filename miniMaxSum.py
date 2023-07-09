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
    # Write your code here
    
    minSum = float('inf')
    maxSum = float('-inf')

    for i in range(len(arr)):
        totalSum = sum(arr) - arr[i]
        minSum = min(minSum, totalSum)
        maxSum = max(maxSum, totalSum)

    print(minSum, maxSum)    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

