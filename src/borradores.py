### --------------------------------------------------
### 7.5 Problem 5: Password strength classifier
### --------------------------------------------------
"""
Descripción:
Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas (puedes afinarlas, 
pero documéntalas en los comentarios).

Ejemplo de reglas:
YA - Weak: longitud < 8 o todo en minúsculas o muy simple.
YA - Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
- Strong: longitud >= 8 y contiene al menos:
  - una letra mayúscula,
  - una letra minúscula,
  - un dígito,
  - un símbolo no alfanumérico (por ejemplo, !, @, #, etc.).

  Operaciones clave sugeridas:
- Recorrer carácter por carácter.
- Métodos: isupper(), islower(), isdigit(), isalnum().
- Uso de banderas booleanas (has_upper, has_lower, etc.).

list()
"""
password_input = input(f"Set a password to evalue: ")
# Separar la contraseña dada en una lista
letter_list = list(password_input)

# Verificar si hay algo d esto
has_upper = any(letter.isupper() for letter in letter_list)
has_digit = any(letter.isdigit() for letter in letter_list)
validation_medium_list = [has_upper, has_digit]
validation_medium = any(validation_list)


# MEDIUM
if len(password_input) >= 8 and validation_medium == True:
    print("medium") 

# WEAK
elif len(password_input) < 8 or password_input.islower() == True:
    print("weak")