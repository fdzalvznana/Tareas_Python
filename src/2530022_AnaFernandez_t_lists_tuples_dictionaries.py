#### PORTADA
"""
Ana Fernanda Sofia Fernandez Alvarez
2530022
IM 1-1
"""
#### RESUMEN
"""
En Python, una lista, una tupla y un diccionario son estructuras de datos: las listas y tuplas guardan elementos ordenados,
pero las listas son mutables (se pueden modificar) mientras que las tuplas son inmutables 
(no cambian una vez creadas).

Un diccionario almacena pares clave–valor, permitiendo acceder a la información 
mediante una clave en lugar de un índice.
La mutabilidad de las listas facilita agregar, quitar o editar datos, 
mientras que la inmutabilidad de las tuplas ofrece seguridad y estabilidad.

Los diccionarios se usan para asociar información, como nombres con teléfonos o productos con precios.
El documento cubrirá la descripción de cada problema, el diseño de entradas y salidas, las validaciones aplicadas
y el uso de listas, tuplas y diccionarios en contextos prácticos como catálogos, registros y estadísticas.
"""
### --------------------------------------------------
### 7.1 Problem 1: Shopping list basics (list operations)
### --------------------------------------------------
"""
Descripción:
Trabaja con una lista de productos (strings) y sus cantidades (enteros). El programa debe:
1) Crear una lista inicial de productos.
2) Permitir agregar un nuevo producto al final.
3) Mostrar la cantidad total de elementos en la lista.
4) Verificar si un producto específico está en la lista (booleano is_in_list).

Validaciones:
- initial_items_text no vacío tras strip().
- Separar la cadena por comas y eliminar espacios extra en cada elemento.
- new_item y search_item no vacíos.
- Manejar el caso de lista inicial vacía si el estudiante lo decide (documentar decisión).
"""
## Operaciones clave sugeridas:
## - split(), strip(), append(), len(), in.

print(f"\n ------------- PROBLEM 1 -------------")
initial_items_text = input("Enter initial items (comma-separated): ")
new_item = input("Enter a new item to add: ").strip()
search_item = input("Enter an item to search for: ").strip()
if len(initial_items_text.strip()) == 0:
    items_list = []
else:
    items_list = [item.strip() for item in initial_items_text.split(",")]
items_list.append(new_item)
len_list = len(items_list)
is_in_list = search_item in items_list
print(f"Items list: {items_list}")
print(f"Total items: {len_list}")
print(f"Found item: {is_in_list}")
print()

# ------------------------------------------------------------
# CASOS DE PRUEBA (NORMAL, BORDE Y ERROR)
# ------------------------------------------------------------
"""
1) Caso Normal
   Entrada:
       Enter initial items: apple, banana, pear
       Enter new item: mango
       Enter item to search: banana
   Análisis:
       items_list = ["apple","banana","pear","mango"]
       search_item = "banana" → True
   Salida esperada:
       Items list: ['apple', 'banana', 'pear', 'mango']
       Total items: 4
       Found item: True


2) Caso Borde (lista inicial vacía)
   Entrada:
       Enter initial items:
       Enter new item: chips
       Enter item to search: chips
   Análisis:
       initial empty → items_list = []
       luego append("chips") → ["chips"]
       search_item = "chips" → True
   Salida esperada:
       Items list: ['chips']
       Total items: 1
       Found item: True


3) Caso Error / Límite (buscar un elemento que no existe)
   Entrada:
       Enter initial items: milk, bread
       Enter new item: eggs
       Enter item to search: cheese
   Análisis:
       items_list = ["milk", "bread", "eggs"]
       "cheese" no está → False
   Salida esperada:
       Items list: ['milk', 'bread', 'eggs']
       Total items: 3
       Found item: False
"""
### --------------------------------------------------
### 7.2 Problem 2: Points and distances with tuples
### --------------------------------------------------
"""
Descripción:
Usa tuplas para representar dos puntos en un plano 2D: (x1, y1) y (x2, y2). El programa debe:
1) Crear dos tuplas point_a y point_b a partir de entradas numéricas.
2) Calcular la distancia euclidiana entre ambos puntos.
3) Crear una nueva tupla midpoint con el punto medio entre ellos.

Validaciones:
- Verificar que las 4 entradas se puedan convertir a float.
- No se requieren restricciones adicionales en el rango.
"""
## Operaciones clave sugeridas:
## - Creación de tuplas: point_a = (x1, y1), point_b = (x2, y2)
## - Cálculo de distancia: ((x2 - x1)**2 + (y2 - y1)**2)**0.5
## - Cálculo de punto medio: ((x1 + x2)/2, (y1 + y2)/2)

print(f"\n ------------- PROBLEM 2 -------------")
x1_input = input("Enter x1: ")
y1_input = input("Enter y1: ")
x2_input = input("Enter x2: ")
y2_input = input("Enter y2: ")

if not all(isinstance(coord, str) and coord.replace('.', '', 1).replace('-', '', 1).isdigit() for coord in [x1_input, y1_input, x2_input, y2_input]):
    print("Error: invalid input")
    exit()

x1 = float(x1_input)
y1 = float(y1_input)
x2 = float(x2_input)
y2 = float(y2_input)

point_a = (x1, y1)
point_b = (x2, y2)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
print(f"Point A: {point_a}")
print(f"Point B: {point_b}")
print(f"Distance: {distance}")
print(f"Midpoint: {midpoint}")
print()
# ------------------------------------------------------------
# CASOS DE PRUEBA (NORMAL, BORDE, ERROR)
# ------------------------------------------------------------
"""
1) Caso Normal
   Entrada:
       x1 = 0
       y1 = 0
       x2 = 3
       y2 = 4
   Análisis:
       distance = 5
       midpoint = (1.5, 2.0)
   Salida esperada:
       Point A: (0.0, 0.0)
       Point B: (3.0, 4.0)
       Distance: 5.0
       Midpoint: (1.5, 2.0)


2) Caso Borde (puntos iguales → distancia 0)
   Entrada:
       x1 = 2
       y1 = 2
       x2 = 2
       y2 = 2
   Análisis:
       distance = 0
       midpoint = (2, 2)
   Salida esperada:
       Point A: (2.0, 2.0)
       Point B: (2.0, 2.0)
       Distance: 0.0
       Midpoint: (2.0, 2.0)


3) Caso Error (entrada no numérica)
   Entrada:
       x1 = 1
       y1 = abc
       x2 = 5
       y2 = 6
   Razón:
       "abc" no pasa el .isdigit() modificado
   Salida esperada:
       Error: invalid input
"""
### --------------------------------------------------
### 7.3 Problem 3: Product catalog with dictionary
### --------------------------------------------------
"""
Descripción:
Administra un pequeño catálogo de productos usando un diccionario donde:
- clave: nombre del producto (string)
- valor: precio unitario (float)
El programa debe:
1) Crear un diccionario inicial con al menos 3 productos.
2) Leer el nombre de un producto y la cantidad a comprar.
3) Calcular el total a pagar si el producto existe.
4) Si el producto no existe, mostrar un mensaje de error.

Validaciones:
- quantity > 0.
- product_name no vacío tras strip().
- Verificar si product_name está en el diccionario (clave).
"""
## Operaciones clave sugeridas:
## - Definir dict literal: product_prices = {"apple": 10.0, ...}
## - in para verificar existencia de clave.
## - Acceso: unit_price = product_prices[product_name]

print(f"\n ------------- PROBLEM 3 -------------")
product_prices = {
    "apple": 10.0,
    "banana": 6.5,
    "milk": 23.0
}

product_name = input("Producto: ").strip().lower()
quantity_input = input("Cantidad: ")

if product_name == "":
    print("Error: invalid input")
else:
    try:
        quantity = int(quantity_input)
        if quantity <= 0:
            print("Error: invalid input")
        else:
            if product_name in product_prices:
                unit_price = product_prices[product_name]
                total_price = unit_price * quantity

                print("Unit price:", unit_price)
                print("Quantity:", quantity)
                print("Total:", total_price)
            else:
                print("Error: product not found")
    except ValueError:
        print("Error: invalid input")
print()
# ------------------------------------------------------------
# CASOS DE PRUEBA (NORMAL, BORDE, ERROR)
# ------------------------------------------------------------
"""
1) Caso Normal
   Entrada:
       Producto: apple
       Cantidad: 3
   Análisis:
       unit_price = 10.0
       total = 30.0
   Salida esperada:
       Unit price: 10.0
       Quantity: 3
       Total: 30.0


2) Caso Borde (cantidad = 1, mínimo válido)
   Entrada:
       Producto: milk
       Cantidad: 1
   Análisis:
       unit_price = 23.0
       total = 23.0
   Salida esperada:
       Unit price: 23.0
       Quantity: 1
       Total: 23.0


3) Caso Error (producto inexistente)
   Entrada:
       Producto: chocolate
       Cantidad: 2
   Salida esperada:
       Error: product not found

--- Otro error válido ---
   Entrada:
       Producto: apple
       Cantidad: -5
   Salida esperada:
       Error: invalid input
"""
### --------------------------------------------------
### 7.4 Problem 4: Student grades with dict and list
### --------------------------------------------------
"""
Descripción:
Administra las calificaciones de un grupo usando un diccionario:
- clave: nombre del estudiante (string)
- valor: lista de calificaciones (list of float)
El programa debe:
1) Crear un diccionario con al menos 3 estudiantes, cada uno con una lista de calificaciones.
2) Leer el nombre de un estudiante.
3) Calcular el promedio de sus calificaciones.
4) Indicar si el estudiante está aprobado (average >= 70.0) con un booleano is_passed.

Validaciones:
- student_name no vacío tras strip().
- Verificar si student_name es una clave en el diccionario.
- Verificar que la lista de calificaciones no esté vacía antes de calcular el promedio.
"""
## Operaciones clave sugeridas:
## - Diccionario de listas: grades = {"Alice": [90, 85], ...}
## - sum(), len() para promedio.
## - in para verificar clave.

print(f"\n ------------- PROBLEM 4 -------------")
grades = {
    "fulanito": [90.0, 85.5, 88.0],
    "pepito": [70.0, 72.5, 68.0],
    "juanito": [55.0, 60.0, 58.5]
}

student_name = input("Estudiante: ").strip().lower()
if student_name == "":
    print("Error: invalid input")
else:
    if student_name not in grades:
        print("Error: student not found")
    else:
        student_grades = grades[student_name]
        if len(student_grades) == 0:
            print("Error: no grades available")
        else:
            average = sum(student_grades) / len(student_grades)
            is_passed = average >= 70.0

            print("Grades:", student_grades)
            print("Average:", average)
            print("Passed:", str(is_passed).lower())
print()
# ------------------------------------------------------------
# CASOS DE PRUEBA (NORMAL, BORDE, ERROR)
# ------------------------------------------------------------
"""
------------- PROBLEM 4 -------------
Caso 1: NORMAL
Input:
    Estudiante: fulanito
Output esperado:
    Grades: [90.0, 85.5, 88.0]
    Average: 87.83333333333333
    Passed: true

------------- PROBLEM 4 -------------
Caso 2: ERROR (nombre no existe)
Input:
    Estudiante: menganito
Output esperado:
    Error: student not found

------------- PROBLEM 4 -------------
Caso 3: BORDE (input vacío)
Input:
    Estudiante: 
Output esperado:
    Error: invalid input
"""
### --------------------------------------------------
### 7.5 Problem 5: Word frequency counter (list + dict)
### --------------------------------------------------
"""
Descripción:
Cuenta la frecuencia de cada palabra en una oración usando:
- Una lista de palabras.
- Un diccionario donde:
  - clave: palabra (string)
  - valor: frecuencia (int)
El programa debe:
1) Leer una oración.
2) Convertirla a minúsculas y separarla en una lista de palabras.
3) Construir un diccionario de frecuencias.
4) Mostrar el diccionario completo y la palabra más frecuente.

Validaciones:
- sentence no vacía tras strip().
- Manejar signos de puntuación simples si el estudiante decide hacerlo (documentar su decisión, por ejemplo usando replace()).
- Verificar que la lista de palabras no esté vacía.
"""
## Operaciones clave sugeridas:
## - lower(), split()
## - Recorrer la lista y actualizar el diccionario:
## - if word in freq_dict: freq_dict[word] += 1
## - else: freq_dict[word] = 1
## - Uso de un ciclo para encontrar la palabra con mayor frecuencia.

print(f"\n ------------- PROBLEM 5 -------------")
sentence = input("Oración: ").strip()
if sentence == "":
    print("Error: invalid input")
else:
    sentence = sentence.lower()
    sentence = sentence.replace(",", "").replace(".", "")
    words_list = sentence.split()
    if len(words_list) == 0:
        print("Error: no words found")
    else:
        freq_dict = {}

        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
        most_common_word = None
        highest_freq = 0

        for word, count in freq_dict.items():
            if count > highest_freq:
                highest_freq = count
                most_common_word = word

        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)
print()
# ------------------------------------------------------------
# CASOS DE PRUEBA (NORMAL, BORDE, ERROR)
# ------------------------------------------------------------
"""
------------- PROBLEM 5 -------------
Caso 1: NORMAL
Input:
    Oración: Hola hola, hola mundo.
Output esperado:
    Words list: ['hola', 'hola', 'hola', 'mundo']
    Frequencies: {'hola': 3, 'mundo': 1}
    Most common word: hola

------------- PROBLEM 5 -------------
Caso 2: ERROR (input vacío)
Input:
    Oración: 
Output esperado:
    Error: invalid input

------------- PROBLEM 5 -------------
Caso 3: BORDE (oración con solo comas/puntos → sin palabras)
Input:
    Oración: ,,, ...
Output esperado:
    Error: no words found

"""
### --------------------------------------------------
### 7.6 Problem 6: Simple contact book (dictionary CRUD)
### --------------------------------------------------
"""
Descripción:
Implementa un mini "contact book" usando un diccionario donde:
- clave: nombre de contacto (string)
- valor: número de teléfono (string)
El programa debe:
1) Crear un diccionario inicial con algunos contactos.
2) Leer una acción action_text ("ADD", "SEARCH" o "DELETE").
3) Según la acción:
   - "ADD": lee name y phone, agrega o actualiza el contacto.
   - "SEARCH": lee name y muestra el teléfono si existe.
   - "DELETE": lee name y elimina el contacto si existe.
4) Mostrar un mensaje indicando el resultado de la operación.

Validaciones:
- Normalizar action_text a mayúsculas.
- Verificar que action_text sea una de las tres opciones válidas.
- name no vacío tras strip().
- Para "ADD": phone no vacío tras strip().
"""
## Operaciones clave sugeridas:
## - Diccionario: contacts = {"Alice": "1234567890", ...}
## - get(), in, pop()
## - Estructura if/elif para manejar cada acción.

print(f"\n ------------- PROBLEM 6 -------------")
contacts = {
    "Alice": "1234567890",
    "Bob": "9876543210",
    "Carol": "5551234567"
}

action_text = input("Acción (ADD, SEARCH, DELETE): ").strip().upper()
if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action")
else:
    if action_text == "ADD":
        name = input("Nombre: ").strip()
        phone = input("Teléfono: ").strip()

        if name == "" or phone == "":
            print("Error: invalid input")
        else:
            contacts[name] = phone
            print("Contact saved:", name, phone)

    elif action_text == "SEARCH":
        name = input("Nombre: ").strip()

        if name == "":
            print("Error: invalid input")
        else:
            if name in contacts:
                print("Phone:", contacts[name])
            else:
                print("Error: contact not found")

    elif action_text == "DELETE":
        name = input("Nombre: ").strip()

        if name == "":
            print("Error: invalid input")
        else:
            if name in contacts:
                contacts.pop(name)
                print("Contact deleted:", name)
            else:
                print("Error: contact not found")
print()
# ------------------------------------------------------------
# CASOS DE PRUEBA (NORMAL, BORDE, ERROR)
# ------------------------------------------------------------
"""
------------- PROBLEM 6 -------------

Caso 1: NORMAL (ADD)
Input:
    Acción (ADD, SEARCH, DELETE): ADD
    Nombre: Daniel
    Teléfono: 1112223333
Output esperado:
    Contact saved: Daniel 1112223333


------------- PROBLEM 6 -------------

Caso 2: ERROR (acción inválida)
Input:
    Acción (ADD, SEARCH, DELETE): UPDATE
Output esperado:
    Error: invalid action


------------- PROBLEM 6 -------------

Caso 3: BORDE (SEARCH con nombre vacío)
Input:
    Acción (ADD, SEARCH, DELETE): SEARCH
    Nombre: 
Output esperado:
    Error: invalid input

"""
# -------------------------------------------------------------------------
#### CONCLUSIONES
"""
- Las listas son convenientes cuando necesito una colección flexible 
donde pueda agregar o eliminar elementos fácilmente.

- Las tuplas resultan útiles cuando quiero asegurar que ciertos datos permanezcan fijos y no se modifiquen accidentalmente.
- Los diccionarios destacan cuando necesito buscar información rápidamente usando claves en lugar de índices numéricos.

Al trabajar con estas estructuras noté patrones comunes, como usar diccionarios que contienen listas 
para agrupar datos relacionados.
También observé que cada estructura resuelve diferentes necesidades: flexibilidad, estabilidad o acceso eficiente.
Elegir la estructura correcta hace que el manejo de datos sea más claro, organizado y eficiente en cada problema.
"""
#### REFERENCIAS
"""
1) Python documentation - Built-in Types: list, tuple, dict 
2) “Lists vs Tuples in Python” — comparación clara entre list y tuple 
3) “Python Data Structures: Lists, Dictionaries, Sets, Tuples” — visión general de estructuras en Python 
4) Tutorial “¿Qué son las listas, tuplas y diccionarios en Python?” (sitio Pontia) 
5) Artículo “Cómo usar listas, diccionarios, tuplas y sets en Python” — explicación sencilla y práctica 
"""