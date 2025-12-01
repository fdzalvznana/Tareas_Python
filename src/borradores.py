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
# Operaciones clave sugeridas: strip(), split(), title(), concatenación, len().
"""
strip: quita espacios
split: separa un string en lista
title: mayusculas al principio
len: longitud pseint pero en python
"""
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
    