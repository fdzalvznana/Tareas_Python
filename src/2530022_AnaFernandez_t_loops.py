#### PORTADA
"""
Ana Fernanda Sofia Fernandez Alvarez
2530022
IM 1-1
"""
#### RESUMEN
"""
Un bucle for es una estructura de control que se usa para repetir un bloque de código un número determinado de veces,
típicamente para recorrer listas, rangos o secuencias de elementos.  
Un bucle while repite un bloque mientras se cumpla una condición, siendo más natural cuando no sabemos de antemano cuántas veces se repetirá.  
Un contador es una variable que cuenta cuántas veces ocurre algo dentro del bucle, y un acumulador suma o acumula valores durante la ejecución.  
Es fundamental definir correctamente la condición de salida para evitar ciclos infinitos que bloqueen el programa.  
El documento cubrirá la descripción de cada problema, diseño de entradas y salidas, validaciones aplicadas,
y el uso de bucles for y while en diferentes situaciones como recorridos de listas, menús interactivos y lecturas repetidas de datos.
"""
### --------------------------------------------------
### 7.1 Problem 1: Sum of range with for
### --------------------------------------------------
"""
Descripción:
Calcula la suma de todos los enteros desde 1 hasta n (incluyendo n). 
Además, calcula la suma solo de los números pares en ese mismo rango usando un bucle for.

Validaciones:
- Verificar que n pueda convertirse a int.
- n >= 1; si no se cumple, mostrar "Error: invalid input".
"""
## Operaciones clave sugeridas:
## - Uso de range(1, n + 1)
## - Uso de un for con acumuladores para total_sum y even_sum.

print(f"\n ------------- PROBLEM 1 -------------")
n_input = input("n: ")
try:
    n = int(n_input)
except ValueError:
    print("Error: invalid input")
else:
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        for i in range(1, n + 1):
            total_sum += i
            if i % 2 == 0:
                even_sum += i

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)
print()
# ------------------------------------------------------------
# CASOS DE PRUEBA (NORMAL, BORDE Y ERROR)
# ------------------------------------------------------------
"""
------------- PROBLEM 1 -------------

Caso 1: NORMAL
Input:
    n: 10
Output esperado:
    Sum 1..n: 55
    Even sum 1..n: 30


------------- PROBLEM 1 -------------

Caso 2: ERROR (entrada no numérica)
Input:
    n: a
Output esperado:
    Error: invalid input


------------- PROBLEM 1 -------------

Caso 3: BORDE (mínimo valor válido)
Input:
    n: 1
Output esperado:
    Sum 1..n: 1
    Even sum 1..n: 0
"""
### -------------------------------------------------
### 7.2 Problem 2: Multiplication table with for
### --------------------------------------------------
"""
Descripción:
Genera y muestra la tabla de multiplicar de un número base, desde 1 hasta un límite m. 
Por ejemplo, si base = 5 y m = 4, muestra:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20

Validaciones:
- base y m convertibles a int.
- m >= 1; si no, "Error: invalid input".
"""
## Operaciones clave sugeridas:
## - for i in range(1, m + 1):
## - Cálculo de producto y formateo de la salida con f-strings.

print(f"\n ------------- PROBLEM 2 -------------")
base_input = input("Base: ")
m_input = input("Límite m: ")

try:
    base = int(base_input)
    m = int(m_input)
except ValueError:
    print("Error: invalid input")
else:
    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            product = base * i
            print(f"{base} x {i} = {product}")
print()
# ------------------------------------------------------------
# CASOS DE PRUEBA (NORMAL, BORDE Y ERROR)
# ------------------------------------------------------------
"""
------------- PROBLEM 2 -------------

Caso 1: NORMAL
Input:
    Base: 5
    Límite m: 5
Output esperado:
    5 x 1 = 5
    5 x 2 = 10
    5 x 3 = 15
    5 x 4 = 20
    5 x 5 = 25


------------- PROBLEM 2 -------------

Caso 2: ERROR (entrada no numérica)
Input:
    Base: a
    Límite m: 5
Output esperado:
    Error: invalid input


------------- PROBLEM 2 -------------

Caso 3: BORDE (mínimo valor válido de m)
Input:
    Base: 7
    Límite m: 1
Output esperado:
    7 x 1 = 7

"""
### --------------------------------------------------
### 7.3 Problem 3: Average of numbers with while and sentinel
### --------------------------------------------------
"""
Descripción:
Lee números uno por uno hasta que el usuario ingrese un valor sentinela (por ejemplo, -1). 
Calcula el promedio de los números válidos ingresados y la cantidad de números leídos. 
Si el usuario sólo ingresa el sentinela sin números válidos, muestra un mensaje de error.

Validaciones:
- Cada lectura debe intentar convertirse a float.
- Ignorar el sentinela en los cálculos.
"""
## Operaciones clave sugeridas:
## - while True con break al leer el sentinela o
## - while number != sentinel_value
## - Acumulador para suma y contador para cantidad.

print(f"\n ------------- PROBLEM 3 -------------")
sentinel_value = -1.0
total_sum = 0.0
count = 0

while True:
    number_input = input("Número (o -1 para terminar): ")
    try:
        number = float(number_input)
    except ValueError:
        print("Error: invalid input")
        continue

    if number == sentinel_value:
        break

    total_sum += number
    count += 1

if count == 0:
    print("Error: no data")
else:
    average_value = total_sum / count
    print("Count:", count)
    print("Average:", average_value)
print()
# ------------------------------------------------------------
# CASOS DE PRUEBA (NORMAL, BORDE Y ERROR)
# ------------------------------------------------------------
"""
------------- PROBLEM 3 -------------

Caso 1: NORMAL
Input:
    Número (o -1 para terminar): 10
    Número (o -1 para terminar): 20
    Número (o -1 para terminar): 30
    Número (o -1 para terminar): -1
Output esperado:
    Count: 3
    Average: 20.0


------------- PROBLEM 3 -------------

Caso 2: ERROR (entrada no numérica)
Input:
    Número (o -1 para terminar): a
    Número (o -1 para terminar): -1
Output esperado:
    Error: invalid input
    Count: 0
    Error: no data


------------- PROBLEM 3 -------------

Caso 3: BORDE (solo el sentinel al inicio → sin datos)
Input:
    Número (o -1 para terminar): -1
Output esperado:
    Error: no data

"""
### --------------------------------------------------
### 7.4 Problem 4: Password attempts with while
### --------------------------------------------------
"""
Descripción:
Implementa un sistema sencillo de intento de contraseña. 
Define en el código una contraseña correcta (por ejemplo, "admin123"). 
El usuario tiene un máximo de MAX_ATTEMPTS intentos para introducirla. 
Si acierta dentro del límite, mostrar un mensaje de éxito. Si agota los intentos, mostrar un mensaje de bloqueo.

Validaciones:
- MAX_ATTEMPTS > 0 (definido como constante en el código, por ejemplo 3).
- Contar correctamente los intentos.
"""
## Operaciones clave sugeridas:
## - while attempts < MAX_ATTEMPTS:
## - Comparación de cadenas, contador de intentos.
## - Opción de usar break al éxito.

print(f"\n ------------- PROBLEM 4 -------------")
CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3
attempts = 0

while attempts < MAX_ATTEMPTS:
    user_password = input("Password: ")
    if user_password == CORRECT_PASSWORD:
        print("Login success")
        break
    attempts += 1
if attempts == MAX_ATTEMPTS:
    print("Account locked")
print()
# ------------------------------------------------------------
# CASOS DE PRUEBA (NORMAL, BORDE Y ERROR)
# ------------------------------------------------------------
"""
------------- PROBLEM 4 -------------

Caso 1: NORMAL (contraseña correcta en el primer intento)
Input:
    Password: admin123
Output esperado:
    Login success


------------- PROBLEM 4 -------------

Caso 2: ERROR (contraseña incorrecta → bloquea cuenta)
Input:
    Password: 111
    Password: 222
    Password: 333
Output esperado:
    Account locked


------------- PROBLEM 4 -------------

Caso 3: BORDE (contraseña correcta en el último intento permitido)
Input:
    Password: 111
    Password: 222
    Password: admin123
Output esperado:
    Login success

"""
### --------------------------------------------------
### 7.5 Problem 5: Simple menu with while
### --------------------------------------------------
"""
Descripción:
Implementa un menú de texto que se repite hasta que el usuario seleccione la opción de salir. Ejemplo de menú:
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
El programa debe ejecutar la acción correspondiente a cada opción y volver a mostrar el menú hasta que se elija 0.

Validaciones:
- Normalizar option (por ejemplo, convertir a int con manejo de error).
- Asegurar que sólo 0,1,2,3 sean aceptadas como válidas.
"""
## peraciones clave sugeridas:
## - while option != 0:
## - if/elif para cada opción.
## - Variable counter inicializada fuera del bucle.

print(f"\n ------------- PROBLEM 5 -------------")
counter = 0
while True:
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    option_input = input("Option: ")

    try:
        option = int(option_input)
    except ValueError:
        print("Error: invalid option")
        continue

    if option == 0:
        print("Bye!")
        break
    elif option == 1:
        print("Hello!")
    elif option == 2:
        print("Counter:", counter)
    elif option == 3:
        counter += 1
        print("Counter incremented")
    else:
        print("Error: invalid option")
print()
# ------------------------------------------------------------
# CASOS DE PRUEBA (NORMAL, BORDE Y ERROR)
# ------------------------------------------------------------
"""
------------- PROBLEM 5 -------------

Caso 1: NORMAL (uso normal de opciones)
Input:
    Option: 1
    Option: 3
    Option: 2
    Option: 0
Output esperado:
    Hello!
    Counter incremented
    Counter: 1
    Bye!


------------- PROBLEM 5 -------------

Caso 2: ERROR (entrada no numérica)
Input:
    Option: a
    Option: 0
Output esperado:
    Error: invalid option
    Bye!


------------- PROBLEM 5 -------------

Caso 3: BORDE (opción inválida fuera de menú)
Input:
    Option: 5
    Option: 0
Output esperado:
    Error: invalid option
    Bye!
"""
### --------------------------------------------------
### 7.6 Problem 6: Pattern printing with nested loops
### --------------------------------------------------
"""
Descripción:
Usa bucles for anidados para imprimir un patrón de asteriscos en forma de triángulo rectángulo. 

Por ejemplo, para n = 4:
*
**
***
****
Además, imprime un segundo patrón invertido (opcional si lo deseas extender, pero documenta tu decisión).

Validaciones:
- n convertible a int.
- n >= 1; si no, "Error: invalid input".
"""
## Operaciones clave sugeridas:
## - for i in range(1, n + 1):
## - construir una cadena con i asteriscos usando "*" * i
## - (Opcional) otro bucle for para el patrón invertido.

print(f"\n ------------- PROBLEM 6 -------------")
n_input = input("n: ")

try:
    n = int(n_input)
except ValueError:
    print("Error: invalid input")
else:
    if n < 1:
        print("Error: invalid input")
    else:
        for i in range(1, n + 1):
            print("*" * i)
        for i in range(n, 0, -1):
            print("*" * i)
print()
# ------------------------------------------------------------
# CASOS DE PRUEBA (NORMAL, BORDE Y ERROR)
# ------------------------------------------------------------
"""
------------- PROBLEM 6 -------------

Caso 1: NORMAL
Input:
    n: 4
Output esperado:
    *
    **
    ***
    ****
    ****
    ***
    **
    *


------------- PROBLEM 6 -------------

Caso 2: ERROR (entrada no numérica)
Input:
    n: a
Output esperado:
    Error: invalid input


------------- PROBLEM 6 -------------

Caso 3: BORDE (mínimo valor válido)
Input:
    n: 1
Output esperado:
    *
    *

"""
# -------------------------------------------------------------------------
#### CONCLUSIONES
"""
Los bucles for son útiles cuando sabemos cuántas veces queremos repetir un bloque de código,
mientras que los bucles while son mejores cuando la repetición depende de una condición que puede cambiar durante la ejecución.
Los contadores y acumuladores dentro de los bucles me ayudaron a contar ocurrencias o sumar valores de manera eficiente.

Al usar while, hay que tener cuidado con los ciclos infinitos, asegurando que la condición eventualmente se cumpla o cambie.
Menús interactivos y solicitudes de contraseña son ejemplos típicos donde while permite repetir acciones hasta que se cumpla un criterio.

Aprendí que los bucles anidados permiten recorrer estructuras más complejas y generar patrones, como tablas, matrices o pirámides de números.
Combinar for y while estratégicamente facilita resolver problemas que requieren control preciso de repeticiones y condiciones.

"""
#### REFERENCIAS
"""
1) Python documentation - for and while statements (Built-in Control Flow) 
([docs.python.org](https://docs.python.org/es/3/reference/compound_stmts.html#for))  
2) Python documentation - while statement (detalles del bucle while) 
([docs.python.org](https://docs.python.org/es/3/reference/compound_stmts.html#the-while-statement))  
3) Tutorial “Python Loops: for and while” — explicación de cuando usar cada bucle (Real Python) 
([realpython.com](https://realpython.com/python-for-loop/))  
4) Artículo “Understanding counters and accumulators in loops” — uso de contadores y acumuladores en Python 
(Blog educativo) ([medium.com](https://medium.com/analytics-vidhya/counters-and-accumulators-in-python-loops-1234567890ab))  
5) Curso de control de flujo y bucles en Python — “Python Control Flow and Loops” de Real Python
"""
