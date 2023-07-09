import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n = len(arr)
    positive = negative = zero = 0

    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1
    
    print("{:.6f}".format(positive/n))  # Imprimir la proporción de números positivos
    print("{:.6f}".format(negative/n))  # Imprimir la proporción de números negativos
    print("{:.6f}".format(zero/n))  # Imprimir la proporción de ceros

if __name__ == '__main__':
    n = int(input().strip())  # Leer el número de elementos en la lista

    arr = list(map(int, input().rstrip().split()))  # Leer la lista de enteros

    plusMinus(arr)  # Llamar a la función plusMinus pasando la lista como argumento
