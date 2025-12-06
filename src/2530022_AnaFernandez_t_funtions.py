#### PORTADA
"""
Ana Fernanda Sofia Fernandez Alvarez
2530022
IM 1-1
"""
#### RESUMEN
"""
Una función en Python es un bloque de código reutilizable que realiza una tarea específica.
Los parámetros son variables definidas en la función, mientras que los argumentos son los valores reales que se envían al llamarla.
Separar la lógica en funciones permite reutilizar código, mantener el programa organizado y facilitar futuras modificaciones.
Un valor de retorno es el resultado que la función envía de vuelta al programa; es mejor retornarlo que solo imprimirlo,
porque así el dato puede usarse en cálculos, validaciones o pruebas.
Este documento cubrirá la descripción de cada problema, el diseño de las funciones utilizadas,
las entradas y salidas esperadas, las validaciones aplicadas y los casos de prueba básicos realizados.

"""
#### PROBLEMAS
### --------------------------------------------------
### 7.1 Problem 1: Rectangle area and perimeter (basic functions)
### --------------------------------------------------
"""
Descripción:
Define dos funciones:
- calculate_area(width, height): regresa el área de un rectángulo.
- calculate_perimeter(width, height): regresa el perímetro.
El código principal debe leer (o definir) los valores, llamar a las funciones y mostrar los resultados.

Validaciones:
- width > 0
- height > 0
- Si alguna condición no se cumple, mostrar "Error: invalid input" y no llamar a las funciones.
"""
# Operaciones clave sugeridas:
# - area = width * height
# - perimeter = 2 * (width + height)

def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)
    
print(f"\n ------------- PROBLEM 1 -------------")
width_input = input("Width: ")
height_input = input("Height: ")

try:
    width = float(width_input)
    height = float(height_input)
except ValueError:
    print("Error: invalid input")
else:
    if width <= 0 or height <= 0:
        print("Error: invalid input")
    else:
        area_value = calculate_area(width, height)
        perimeter_value = calculate_perimeter(width, height)
        print("Area:", area_value)
        print("Perimeter:", perimeter_value)
print()
## ----- CASOS DE PRUEBA -----
"""
1) Caso NORMAL
Entrada:
Width: 4
Height: 6
Salida esperada:
Area: 24.0
Perimeter: 20.0

2) Caso ERROR (valor no numérico)
Entrada:
Width: hola
Height: 5
Salida esperada:
Error: invalid input

3) Caso BORDE (valor mínimo válido > 0)
Entrada:
Width: 0.0001
Height: 0.0001
Salida esperada:
Area: 1e-08
Perimeter: 0.0002
"""
### --------------------------------------------------
### 7.2 Problem 2: Grade classifier (function with return string)
### --------------------------------------------------
"""
Descripción:
Define una función classify_grade(score) que reciba una calificación numérica (0–100) y regrese una categoría:
- "A" si score >= 90
- "B" si 80 <= score < 90
- "C" si 70 <= score < 80
- "D" si 60 <= score < 70
- "F" si score < 60
El código principal debe llamar la función y mostrar el resultado.

Validaciones:
- 0 <= score <= 100
- Si no se cumple, mostrar "Error: invalid input" y no clasificar.
"""
# Operaciones clave sugeridas:
# - if/elif para rangos.
# - Función con un único return al final o varios returns (pero bien documentados).

def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
print(f"\n ------------- PROBLEM 2 -------------")
score_input = input("Score: ")

try:
    score = float(score_input)
except ValueError:
    print("Error: invalid input")
else:
    if score < 0 or score > 100:
        print("Error: invalid input")
    else:
        grade_letter = classify_grade(score)
        print("Score:", score)
        print("Category:", grade_letter)

## ----- CASOS DE PRUEBA -----
"""
1) Caso NORMAL
Entrada:
Score: 85
Salida esperada:
Score: 85.0
Category: B

2) Caso ERROR (dato fuera de rango)
Entrada:
Score: 150
Salida esperada:
Error: invalid input

3) Caso BORDE (límite exacto entre categorías)
Entrada:
Score: 90
Salida esperada:
Score: 90.0
Category: A
"""
### --------------------------------------------------
### 7.3 Problem 3: List statistics function (min, max, average)
### --------------------------------------------------
"""
Descripción:
Define una función summarize_numbers(numbers_list) que reciba una lista de números y regrese un diccionario con:
- "min": mínimo
- "max": máximo
- "average": promedio (float)
El código principal debe construir la lista (por ejemplo, a partir de texto separado por comas), llamar la función y mostrar los valores.

Validaciones:
- numbers_text no vacío tras strip().
- Lista no vacía después de la conversión.
- Todos los elementos deben poder convertirse a números; si alguno falla, mostrar "Error: invalid input".
"""
# Operaciones clave sugeridas:
# - split() para construir la lista de strings.
# - Conversión a float o int dentro de un ciclo.
# - sum(), len(), min(), max() dentro de summarize_numbers().

def summarize_numbers(numbers_list):
    result = {}
    result["min"] = min(numbers_list)
    result["max"] = max(numbers_list)
    result["average"] = sum(numbers_list) / len(numbers_list)
    return result
print(f"\n ------------- PROBLEM 3 -------------")
numbers_text = input("Numbers (comma separated): ").strip()

if numbers_text == "":
    print("Error: invalid input")
else:
    parts = numbers_text.split(",")
    numbers_list = []

    for p in parts:
        p = p.strip()
        try:
            num = float(p)
        except ValueError:
            print("Error: invalid input")
            break
        numbers_list.append(num)
    else:
        if len(numbers_list) == 0:
            print("Error: invalid input")
        else:
            summary = summarize_numbers(numbers_list)
            print("Min:", summary["min"])
            print("Max:", summary["max"])
            print("Average:", summary["average"])

## ----- CASOS DE PRUEBA -----
"""
1) Caso NORMAL
Entrada:
Numbers (comma separated): 3, 10, 5, 2

Salida esperada:
Min: 2.0
Max: 10.0
Average: 5.0

2) Caso ERROR (valor no numérico)
Entrada:
Numbers (comma separated): 4, abc, 8

Salida esperada:
Error: invalid input

3) Caso BORDE (un solo número)
Entrada:
Numbers (comma separated): 7

Salida esperada:
Min: 7.0
Max: 7.0
Average: 7.0
"""
### --------------------------------------------------
### 7.4 Problem 4: Apply discount list (pure function)
### --------------------------------------------------
"""
Descripción:
Define una función apply_discount(prices_list, discount_rate) que:
- reciba una lista de precios (float) y una tasa de descuento (por ejemplo, 0.10 para 10%)
- regrese una nueva lista con los precios ya descontados (no modificar la lista original).
El código principal debe:
- Crear una lista de precios.
- Llamar a la función.
- Mostrar la lista original y la nueva lista con descuento.
 Validaciones:
- prices_text no vacío y lista resultante no vacía.
- Todos los precios > 0.
- 0 <= discount_rate <= 1; si no, "Error: invalid input".
"""
# Operaciones clave sugeridas:
# - Construir la lista de float desde texto.
# - En la función, usar un ciclo para crear una nueva lista:
# - discounted_price = price * (1 - discount_rate)
# - No modificar la lista de entrada (pure function).

def apply_discount(prices_list, discount_rate):
    discounted = []
    for price in prices_list:
        new_price = price * (1 - discount_rate)
        discounted.append(new_price)
    return discounted
print(f"\n ------------- PROBLEM 4 -------------")
prices_text = input("Prices (comma separated): ").strip()
discount_input = input("Discount rate (0–1): ")

if prices_text == "":
    print("Error: invalid input")
else:
    parts = prices_text.split(",")
    prices_list = []

    for p in parts:
        p = p.strip()
        try:
            price = float(p)
        except ValueError:
            print("Error: invalid input")
            break
        if price <= 0:
            print("Error: invalid input")
            break
        prices_list.append(price)
    else:
        if len(prices_list) == 0:
            print("Error: invalid input")
        else:
            try:
                discount_rate = float(discount_input)
            except ValueError:
                print("Error: invalid input")
            else:
                if discount_rate < 0 or discount_rate > 1:
                    print("Error: invalid input")
                else:
                    discounted_list = apply_discount(prices_list, discount_rate)
                    print("Original prices:", prices_list)
                    print("Discounted prices:", discounted_list)
## ----- CASOS DE PRUEBA -----
"""
CASO 1 — Normal
----------------
Prices (comma separated): 100, 250, 50
Discount rate (0-1): 0.2
Original prices: [100.0, 250.0, 50.0]
Discounted prices: [80.0, 200.0, 40.0]

CASO 2 — Error (precio inválido)
--------------------------------
Prices (comma separated): 10, -5, 20
Discount rate (0-1): 0.3
Error: invalid input

CASO 3 — Borde (un solo precio, sin descuento)
----------------------------------------------
Prices (comma separated): 99.99
Discount rate (0-1): 0
Original prices: [99.99]
Discounted prices: [99.99]
"""
### --------------------------------------------------
### 7.5 Problem 5: Greeting function with default parameters
### --------------------------------------------------
"""
Descripción:
Define una función greet(name, title="") que:
- Concatene opcionalmente el título antes del nombre (por ejemplo, "Dr. Alice", "Eng. Bob").
- Regrese el mensaje: "Hello, <full_name>!"
Si title está vacío, solo usar el nombre. El código principal debe llamar a la función usando argumentos posicionales y nombrados.

Validaciones:
- name no vacío tras strip().
- title puede estar vacío, pero si no lo está, también se normaliza con strip().
"""
# Operaciones clave sugeridas:
# - Uso de parámetros con valor por defecto: def greet(name, title=""):
# - Uso de argumentos nombrados: greet(name="Alice", title="Dr.")

def greet(name, title=""):
    name = name.strip()
    title = title.strip()
    if not name:
        print("Error: invalid input")
        return None
    full_name = f"{title} {name}".strip()
    return f"Hello, {full_name}!"
print(f"\n ------------- PROBLEM 5 -------------")
name_input = input("Name: ")
title_input = input("Title (optional): ")

greeting = greet(name_input, title_input)

if greeting is not None:
    print("Greeting:", greeting)

# ----- CASOS DE PRUEBA -----
"""
# CASO NORMAL
Entrada:
Name: Juan
Title (optional): Mr.
Salida esperada:
Greeting: Hello, Mr. Juan!

# CASO ERROR (nombre vacío)
Entrada:
Name:
Title (optional): Dr.
Salida esperada:
Error: invalid input

# CASO BORDE (sin título)
Entrada:
Name: Ana
Title (optional):
Salida esperada:
Greeting: Hello, Ana!
"""
### --------------------------------------------------
### 7.6 Problem 6: Factorial function (iterative or recursive)
### --------------------------------------------------
"""
Descripción:
Define una función factorial(n) que regrese n! (n factorial). Puedes implementarla de forma iterativa (con for) o recursiva, pero debes documentar tu elección en comentarios. El código principal debe:
- Leer/definir n.
- Validar n.
- Llamar a factorial(n).
- Mostrar el resultado.

Validaciones:
- n entero.
- n >= 0.
- Opcional: limitar n a un máximo razonable (por ejemplo n <= 20) 
para evitar números demasiado grandes; si no se cumple, mostrar "Error: invalid input".
"""
# Operaciones clave sugeridas:
# - Versión iterativa:
# - result = 1
# - for i in range(1, n + 1): result *= i
# - Versión recursiva (opcional):
# - factorial(0) = 1
# - factorial(n) = n * factorial(n - 1)

def factorial(n):
    # Implementación iterativa (elegida por eficiencia y para evitar límites de recursión)
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"\n ------------- PROBLEM 6 -------------")
n_input = input("n: ")

try:
    n = int(n_input)
except ValueError:
    print("Error: invalid input")
else:
    if n < 0 or n > 20:
        print("Error: invalid input")
    else:
        value = factorial(n)
        print("n:", n)
        print("Factorial:", value)

# ----- CASOS DE PRUEBA -----
"""
# CASO NORMAL
Entrada:
n: 5
Salida esperada:
n: 5
Factorial: 120

# CASO ERROR (valor fuera de rango)
Entrada:
n: 25
Salida esperada:
Error: invalid input

# CASO BORDE (límite inferior válido)
Entrada:
n: 0
Salida esperada:
n: 0
Factorial: 1
"""
# -------------------------------------------------------------------------
#### CONCLUSIONES
"""
Las funciones permiten organizar mejor el código al separar tareas específicas en bloques reutilizables,
lo que hace que el programa sea más claro y más fácil de mantener. Devolver valores con return es ventajoso
porque permite usar los resultados en otros cálculos o procesos, en lugar de limitarse solo a mostrarlos.
El uso de parámetros y valores por defecto también hace el código más flexible, ya que una misma función
puede adaptarse a diferentes situaciones sin necesidad de duplicar código. Me resultó especialmente útil
encapsular lógica en funciones cuando necesitaba repetir cálculos o aplicar validaciones varias veces.
Además, aprendí a distinguir entre la lógica principal del programa y las funciones de apoyo, entendiendo
cómo estas últimas ayudan a mantener el flujo del programa limpio y bien estructurado.
"""
#### REFERENCIAS
# 1) Documentación oficial de Python – Definición de funciones (en español):
#    https://docs.python.org/es/3/tutorial/controlflow.html#defining-functions
# 2) AprendePython.org – Funciones en Python:
#    https://aprendepython.org/funciones/
# 3) Programiz en español – Guía de funciones en Python:
#    https://www.programiz.com/python-programming/function (traducible automáticamente desde navegador)
# 4) KeepCoding – Funciones en Python: explicación y ejemplos:
#    https://keepcoding.io/blog/funciones-en-python/
# 5) CódigoFacilito – Curso de Python: funciones y parámetros:
#    https://codigofacilito.com/articulos/funciones-python
