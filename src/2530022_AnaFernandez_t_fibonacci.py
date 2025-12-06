#### PORTADA
"""
Ana Fernanda Sofia Fernandez Alvarez
2530022
IM 1-1
"""
#### RESUMEN
"""
La serie de Fibonacci es una secuencia donde cada término se obtiene sumando los dos anteriores, comenzando por 0 y 1.  
Calcular la serie hasta un número de términos n significa generar los primeros n valores siguiendo esa regla.  
El programa leerá el valor de n ingresado por el usuario, aplicará una validación básica para asegurar que sea positivo,
y luego generará la serie completa mostrando cada término en orden.  
"""
#### PROBLEMA
"""
Un programa en Python que calcule y muestre la serie de Fibonacci hasta un número de términos 
dado por el usuario, utilizando variables, validación de entrada y al menos un bucle (for o while). 
Además, que documente su solución con descripción, casos de prueba y conclusiones.
"""
print("\n------------- PROBLEM 6.1: FIBONACCI SERIES -------------")
n_input = input("n: ")

try:
    n = int(n_input)
except ValueError:
    print("Error: invalid input")
else:
    if n < 1 or n > 50:
        print("Error: invalid input")
    else:
        fib_series = []
        if n >= 1:
            fib_series.append(0)
        if n >= 2:
            fib_series.append(1)
        for i in range(2, n):
            next_term = fib_series[-1] + fib_series[-2]
            fib_series.append(next_term)

        print("Number of terms:", n)
        print("Fibonacci series:", *fib_series)

## ----- CASOS DE PRUEBA -----
"""
Caso de prueba 1 (borde)
Entrada:
n: 1
Salida esperada:
Number of terms: 1
Fibonacci series: 0

Caso de prueba 2 (normal)
Entrada:
n: 7
Salida esperada:
Number of terms: 7
Fibonacci series: 0 1 1 2 3 5 8

Caso de prueba 3 (error)
Entrada:
n: hola
Salida esperada:
Error: invalid input
"""
#### Conclusiones
"""
El uso de un bucle facilitó generar cada nuevo número de la serie tomando los dos anteriores de forma automática.  
Es importante manejar los casos n = 1 y n = 2 porque esos valores solo requieren mostrar los primeros términos sin cálculos adicionales.  
Esta misma lógica puede reutilizarse en otros programas que necesiten secuencias generadas por reglas, cálculos progresivos o acumulación de valores.  1
"""
#### Referencias
# 1) Python documentation – for and while loops: https://docs.python.org/es/3/reference/compound_stmts.html
# 2) Tutorial “Fibonacci Sequence in Python” (Real Python): https://realpython.com/fibonacci-sequence-python/
# 3) Apuntes de programación básica – estructuras repetitivas y generación de secuencias (mclibre.org): https://www.mclibre.org/consultar/python/