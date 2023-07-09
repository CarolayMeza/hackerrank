#!/bin/python3

import math
import os
import random
import re
import sys

def fizzBuzz(n):
    # Iterar desde 1 hasta n
    for number in range(1, n + 1):
        # Comprobar si es divisible por 3 y 5
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        # Comprobar si es divisible por 3
        elif number % 3 == 0:
            print("Fizz")
        # Comprobar si es divisible por 5
        elif number % 5 == 0:
            print("Buzz")
        # Si no es divisible por 3 ni por 5, imprimir el número
        else:
            print(number)

if __name__ == '__main__':
    # Leer el valor de entrada
    n = int(input().strip())

    # Llamar a la función fizzBuzz con el valor de entrada
    fizzBuzz(n)
