#### PORTADA
"""
Ana Fernanda Sofia Fernandez Alvarez
2530022
IM 1-1
"""
#### RESUMEN
"""
un CRUD (Create, Read, Update, Delete) sobre una estructura de datos en memoria (diccionario y/o lista de diccionarios) 
utilizando funciones en Python. Separar responsabilidades (cada operación en una función), 
el diseño de menús básicos, la validación de entradas y la documentación de su solución con descripción, casos de prueba y 
conclusiones.
"""
#### PROBLEMA
"""
Gestor CRUD usando diccionarios y/o listas con funciones:
Implementar un programa en Python que gestione un conjunto de "items" en memoria mediante operaciones CRUD.
"""
print("\n------------- PROBLEM 6.1: CRUD CON FUNCIONES -------------")
# ----------------------- funciones -----------------------

def create_item(items, item_id, name, price, quantity):
    """Crea un ítem nuevo si el ID no existe. Retorna True si se creó."""
    if item_id in items:
        return False  # No permitir duplicados
    items[item_id] = {
        "id": item_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return True

def read_item(items, item_id):
    """Retorna el ítem si existe, o None si no existe."""
    return items.get(item_id)

def update_item(items, item_id, new_name, new_price, new_quantity):
    """Actualiza un ítem existente. Retorna True si se actualizó."""
    if item_id not in items:
        return False
    items[item_id]["name"] = new_name
    items[item_id]["price"] = new_price
    items[item_id]["quantity"] = new_quantity
    return True

def delete_item(items, item_id):
    """Elimina un ítem si existe. Retorna True si se eliminó."""
    if item_id in items:
        del items[item_id]
        return True
    return False

def list_items(items):
    """Imprime todos los ítems en formato legible."""
    if not items:
        print("No items available.")
        return
    print("\nItems list:")
    for item in items.values():
        print(f"- ID: {item['id']}, Name: {item['name']}, "
              f"Price: {item['price']}, Quantity: {item['quantity']}")
    print()

# ----------------------- MAIN PROGRAM -----------------------

def is_valid_number(value, is_int=False):
    """Convierte y valida números. Retorna número o None."""
    try:
        return int(value) if is_int else float(value)
    except ValueError:
        return None

print("\n------------- CRUD INVENTORY SYSTEM -------------\n")

items = {}  

while True:
    print("\nMENU")
    print("1) Create item")
    print("2) Read item by id")
    print("3) Update item by id")
    print("4) Delete item by id")
    print("5) List all items")
    print("0) Exit")

    option = input("Option: ").strip()

    if option not in {"0", "1", "2", "3", "4", "5"}:
        print("Error: invalid input")
        continue

    if option == "0":
        print("Exiting program...")
        break

    # create
    if option == "1":
        item_id = input("Item ID: ").strip()
        if not item_id:
            print("Error: invalid input")
            continue

        name = input("Name: ").strip()
        if not name:
            print("Error: invalid input")
            continue

        price_input = input("Price: ").strip()
        price = is_valid_number(price_input, is_int=False)
        if price is None or price < 0:
            print("Error: invalid input")
            continue

        qty_input = input("Quantity: ").strip()
        quantity = is_valid_number(qty_input, is_int=True)
        if quantity is None or quantity < 0:
            print("Error: invalid input")
            continue

        if create_item(items, item_id, name, price, quantity):
            print("Item created")
        else:
            print("Error: ID already exists")

    # read
    elif option == "2":
        item_id = input("Item ID: ").strip()
        if not item_id:
            print("Error: invalid input")
            continue

        item = read_item(items, item_id)
        if item:
            print("Item found:")
            print(f"ID: {item['id']}")
            print(f"Name: {item['name']}")
            print(f"Price: {item['price']}")
            print(f"Quantity: {item['quantity']}")
        else:
            print("Item not found")

    # update
    elif option == "3":
        item_id = input("Item ID: ").strip()
        if not item_id:
            print("Error: invalid input")
            continue

        name = input("New name: ").strip()
        if not name:
            print("Error: invalid input")
            continue

        price_input = input("New price: ").strip()
        new_price = is_valid_number(price_input, is_int=False)
        if new_price is None or new_price < 0:
            print("Error: invalid input")
            continue

        qty_input = input("New quantity: ").strip()
        new_quantity = is_valid_number(qty_input, is_int=True)
        if new_quantity is None or new_quantity < 0:
            print("Error: invalid input")
            continue

        if update_item(items, item_id, name, new_price, new_quantity):
            print("Item updated")
        else:
            print("Item not found")

    # borrar item
    elif option == "4":
        item_id = input("Item ID: ").strip()
        if not item_id:
            print("Error: invalid input")
            continue

        if delete_item(items, item_id):
            print("Item deleted")
        else:
            print("Item not found")

    # enlistar
    elif option == "5":
        list_items(items)

## -------------------------
## TEST CASES — CRUD SYSTEM
## -------------------------
"""
===== NORMAL CASES =====
1) Create item (normal)
Option: 1
Item ID: A1
Name: Apple
Price: 10.5
Quantity: 20
Expected: Item created

2) Create another item
Option: 1
Item ID: B2
Name: Banana
Price: 5.0
Quantity: 15
Expected: Item created

3) Read existing item
Option: 2
Item ID: A1
Expected: Show item details (Apple, 10.5, 20)

4) Update existing item
Option: 3
Item ID: B2
New name: Banana Premium
New price: 6.0
New quantity: 30
Expected: Item updated

5) Delete existing item
Option: 4
Item ID: A1
Expected: Item deleted

6) List items (some items exist)
Option: 5
Expected: Show list containing B2 (updated)

===== BORDER CASES =====
7) Create item with price = 0
Option: 1
Item ID: X1
Name: Free Sample
Price: 0
Quantity: 5
Expected: Item created

8) Create item with quantity = 0
Option: 1
Item ID: X2
Name: Empty Stock
Price: 15
Quantity: 0
Expected: Item created

9) Read item immediately after creation
Option: 2
Item ID: X2
Expected: Show item details

10) Update item setting quantity = 0
Option: 3
Item ID: B2
New name: Banana
New price: 5.5
New quantity: 0
Expected: Item updated

11) List when multiple items exist
Option: 5
Expected: Show X1, X2, B2

===== ERROR CASES =====
12) Invalid menu option
Option: 9
Expected: Error: invalid input

13) Create item with empty ID
Option: 1
Item ID: 
Expected: Error: invalid input

14) Create item with negative price
Option: 1
Item ID: C3
Name: BadPrice
Price: -10
Quantity: 5
Expected: Error: invalid input

15) Create item with negative quantity
Option: 1
Item ID: C4
Name: BadQty
Price: 10
Quantity: -3
Expected: Error: invalid input

16) Create duplicate ID
Option: 1
Item ID: B2
Name: Dup
Price: 1
Quantity: 1
Expected: Error: ID already exists

17) Read non-existing item
Option: 2
Item ID: Z9
Expected: Item not found

18) Update non-existing item
Option: 3
Item ID: Z9
New name: Test
New price: 1
New quantity: 1
Expected: Item not found

19) Delete non-existing item
Option: 4
Item ID: Z9
Expected: Item not found

20) Invalid price format
Option: 1
Item ID: D1
Name: WrongPrice
Price: abc
Quantity: 5
Expected: Error: invalid input

21) Invalid quantity format
Option: 1
Item ID: D2
Name: WrongQty
Price: 10.5
Quantity: xyz
Expected: Error: invalid input

22) List items when structure might be empty
(Clear items manually then run)
Option: 5
Expected: No items available.
"""
#### Conclusiones
"""
El uso de funciones hizo que el CRUD fuera más claro y modular, evitando repetir código y separando
la lógica de cada operación. Manejar los datos con un diccionario o una lista de diccionarios facilitó
el acceso por ID y permitió almacenar múltiples campos por elemento de forma ordenada. Uno de los retos
fue validar correctamente las entradas del usuario, especialmente convertir valores numéricos y evitar
IDs vacíos o duplicados; esto se resolvió agregando verificaciones antes de ejecutar cada operación.
Para extender este CRUD a un sistema más grande, podría añadirse persistencia mediante archivos JSON,
CSV o incluso conectarlo a una base de datos, permitiendo guardar los datos entre ejecuciones y
soportar más operaciones avanzadas como búsquedas, filtros o reportes.

"""
#### Referencias
# 1) Python documentation – Data structures (dict, list): https://docs.python.org/3/tutorial/datastructures.html
# 2) Python documentation – Defining functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# 3) Tutorial básico de CRUD en Python (en memoria): https://realpython.com/python-dicts/
