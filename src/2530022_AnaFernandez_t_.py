### --------------------------------------------------
### 7.6 Problem 6: Product label formatter (fixed-width text)
### --------------------------------------------------
"""
Descripción:
Dado el nombre de un producto y su precio, genera una etiqueta en una sola línea con el siguiente formato:

Product: <NAME> | Price: $<PRICE>

La cadena completa debe tener exactamente 30 caracteres:
- Si es más corta, rellena con espacios al final.
- Si es más larga, recorta hasta 30 caracteres.

Operaciones clave sugeridas:
- Uso de f-strings o concatenación para formar la etiqueta base.
- len() para medir la longitud.
- slicing para recortar: label[:30].
- Relleno con espacios hasta alcanzar 30 caracteres.
""" 
print(f"\n ------------- PROBLEM 6 -------------")
product_name = input(f"Product name: ")
price_value = input(f"Product price: ")
normalized_name = product_name.strip()

if len(normalized_name) < 30:
    normalized_name = normalized_name.ljust(30)
else:
    normalized_name = normalized_name[:30]

print(f"Product: {normalized_name.title()} | Price: ${price_value}")



