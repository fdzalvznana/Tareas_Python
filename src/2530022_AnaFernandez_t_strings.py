### PROBLEMAS
## --------------------------------------------------
## 7.1 Problem 1: Full name formatter (name + initials)
## --------------------------------------------------
"""
Descripción:
Dado el nombre completo de una persona en una sola cadena (por ejemplo: "juan carlos tovar"), el programa debe:
1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: J.C.T.).
"""

name_input = input(f"Tell me your full name: ")

name_list = name_input.split()
full_name = f"{name_list[0].lower().strip()} {name_list[1].lower().strip()} {name_list[2].lower().strip()}"

initials = []
for initial in name_list:
    initials.append(initial[0])

full_initials = f"{initials[0]}. {initials[1]}. {initials[2]}."

print(f" Formated Name: {full_name.title()}")
print(f" Initials: {full_initials.title()}")