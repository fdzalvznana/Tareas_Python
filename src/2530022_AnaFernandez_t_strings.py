#### PROBLEMAS
### --------------------------------------------------
### 7.1 Problem 1: Full name formatter (name + initials)
### --------------------------------------------------
"""
Descripción:
Dado el nombre completo de una persona en una sola cadena (por ejemplo: "juan carlos tovar"), el programa debe:
1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: J.C.T.).

Validaciones:
YA - full_name no debe estar vacío después de strip().
YA - Debe contener al menos dos palabras (por ejemplo, nombre y apellido).
YA - No aceptar cadenas que sean solo espacios.
"""
## Operaciones clave sugeridas: strip(), split(), title(), concatenación, len().
# strip: quita espacios
# split: separa un string en lista
# title: mayusculas al principio
# len: longitud pseint pero en python

print(f"\n ------------- PROBLEM 1 -------------")
name_input = input(f"Tell me your name: ")
name_list = name_input.split()

if len(name_list) == 0:
    print("Characters not found.")
elif len(name_list) < 2:
    print("At least a first and last name.")
else:
    full_name = " ".join(name_list)
    initials= []
    for word in name_list:
        initials.append(word[0].title())  
    
    result = ". ".join(initials)
    print(f"Formatted name: {full_name.title()}")
    print(f"Initials: {result}.")

print()

### --------------------------------------------------
### 7.2 Problem 2: Simple email validator (structure + domain)
### --------------------------------------------------
"""
Descripción:
Valida si una dirección de correo tiene un formato básico correcto:
- Contiene exactamente un '@'.
- Después del '@' debe haber al menos un '.'.
- No contiene espacios en blanco.
Si el correo es válido, también muestra el dominio (la parte después de '@').
"""
## Operaciones clave sugeridas: strip(), count(), find(), slicing, in, not in.
# strip: quitar espacios ente palabras
# count: para contar cuántas veces aparece algo
# find: Devuelve la posición donde aparece por primera vez

print(f"\n ------------- PROBLEM 2 -------------")
email_input = input(f"Tell me your email: ")
email_splited = email_input.split()
at_text = email_input.find("@")
final = email_input[at_text:]
dot_valid = final.find(".")

# Valida si hay o no espacios
if len(email_splited) > 1:
    print("No debe de haber espacios") 

# Valida si hay o no un arroba
elif at_text == -1:
    print(f"@ inexistente")

# Valida si hay solo 1 arroba
elif email_input.count("@") > 1:
    print("Debe haber solo un arroba")

# Valida si hay solo 1 punto
elif dot_valid == -1:
    print("Debe tener al menos un '.'")
else:
    print("Your email is valid")
    print(f"Dominion: {final}")
print()

### --------------------------------------------------
### 7.3 Problem 3: Palindrome checker (ignoring spaces and case)
### --------------------------------------------------
"""
Descripción:
Determina si una frase es un palíndromo, es decir, se lee igual de izquierda a derecha y de derecha a izquierda, ignorando espacios y mayúsculas/minúsculas.
Validaciones:
- phrase no vacía tras strip().
- Longitud mínima razonable después de limpiar espacios (por ejemplo, al menos 3 caracteres).
"""
## Operaciones clave sugeridas: lower(), replace(" ", ""), slicing inverso text[::-1], comparación ==.
# lower: minusculas todos
# replace: sirve para reemplazar una parte del texto por otra (" ", "")
# slicing inverso: forma de leer una cadena al revés usando la sintaxis [::-1]
# strip: quitar espacios a los bordes 

print(f"\n ------------- PROBLEM 3 -------------")
phrase_input = input(f"Set your palindrome: ")
modified_phrase = phrase_input.lower().strip().replace(" ", "")
is_palindrome = modified_phrase[::-1]

if len(modified_phrase) < 3:
    print("Your phrase/word must be at least 3 characters long")
elif is_palindrome == modified_phrase:
    is_palindrome = True
    print(f"Normalized Phrase: {modified_phrase}")
    print(f"Is a palindrome: {is_palindrome} ")
else: 
    is_palindrome = False
    print(f"Is not a palindrome: {is_palindrome}")
print()

### --------------------------------------------------
### 7.4 Problem 4: Sentence word stats (lengths and first/last word)
### --------------------------------------------------
"""
Descripción:
Dada una oración, el programa debe:
1) Normalizar espacios (quitar espacios al principio y al final).
2) Separar las palabras por espacios.
3) Mostrar:
   - Número total de palabras.
   YA - Primera palabra.
   YA - Última palabra.
   - Palabra más corta y más larga (por longitud).

Validaciones:
- Oración no vacía tras strip().
- Debe contener al menos una palabra válida después de split().
"""
## Operaciones clave sugeridas: strip(), split(), len(), recorrer la lista de palabras para encontrar mínima y máxima longitud.

print(f"\n ------------- PROBLEM 4 -------------")
phrase_input = input(f"Enter sentence: ")
phrase_list = phrase_input.split()

if len(phrase_input) == 0:
    print("Character not found")
else: 
    longest_word = max(phrase_list, key=len)
    shortest_word = min(phrase_list, key=len)

    print(f"Total number of words: {len(phrase_list)}")
    print(f"First word in sentence: {phrase_list[0]}")
    print(f"Last word in sentence: {phrase_list[-1]}")
    print(f"Longest word: {longest_word}")
    print(f"Shortest word: {shortest_word}")
    print()

### --------------------------------------------------
### 7.5 Problem 5: Password strength classifier
### --------------------------------------------------
"""
Descripción:
Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas (puedes afinarlas, 
pero documéntalas en los comentarios).

Ejemplo de reglas:
- Weak: longitud < 8 o todo en minúsculas o muy simple.
- Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
- Strong: longitud >= 8 y contiene al menos:
  - una letra mayúscula,
  - una letra minúscula,
  - un dígito,
  - un símbolo no alfanumérico (por ejemplo, !, @, #, etc.).
"""
## Operaciones clave sugeridas:
## Recorrer carácter por carácter. 
## - Métodos: isupper(), islower(), isdigit(), isalnum(). 
## - Uso de banderas booleanas (has_upper, has_lower, etc.).

print(f"\n ------------- PROBLEM 5 -------------")
password_input = input(f"Set a password to evalue: ")
# Separar la contraseña dada en una lista
letter_list = list(password_input)

# Verificar si hay algo d esto
has_upper = any(letter.isupper() for letter in letter_list)
has_lower = any(letter.islower() for letter in letter_list)
has_digit = any(letter.isdigit() for letter in letter_list)
has_noalnum = any(not letter.isalnum() for letter in letter_list)

all_lower = all(letter.islower() for letter in letter_list)
all_upper = all(letter.isupper() for letter in letter_list)
all_digit = all(letter.isdigit()  for letter in letter_list)
all_noalnum = all(not letter.isalnum() for letter in letter_list)

# Lista de todo lo verificable
verify_list = [has_upper, has_lower, has_digit, has_noalnum]
verify_all = [all_lower, all_upper, all_digit, all_noalnum]

# Strong - Medium - Weak
if  len(password_input) >= 8 and all(verify_list) == True:
  print("Strong")

elif len(password_input) < 8 or any(verify_all) == True:
  print("Weak")

elif len(password_input) >= 8 and any(verify_list) == True:
  print("Medium")


print()

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
""" 

## Operaciones clave sugeridas:
## - Uso de f-strings o concatenación para formar la etiqueta base.
## - len() para medir la longitud.
## - slicing para recortar: label[:30].
## - Relleno con espacios hasta alcanzar 30 caracteres.

print(f"\n ------------- PROBLEM 6 -------------")
product_name = input(f"Product name: ")
price_value = input(f"Product price: ")
normalized_name = product_name.strip()

if len(normalized_name) < 30:
    normalized_name = normalized_name.ljust(30)
else:
    normalized_name = normalized_name[:30]

print(f"Product: {normalized_name.title()} | Price: ${price_value}")
