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
