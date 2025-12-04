#### PORTADA
"""
Ana Fernanda Sofia Fernandez Alvarez
2530022
IM 1-1
"""
#### RESUMEN
"""
En Python, los tipos int y float representan números: int almacena valores enteros,
mientras que float maneja números con decimales. Un booleano (True/False) es un tipo lógico
que se obtiene mediante comparaciones como ==, !=, >, < o >=, las cuales permiten tomar decisiones.

Validar rangos es importante para evitar datos incorrectos y asegurar que el programa funcione correctamente,
especialmente evitando errores como la división entre cero. 
El documento cubrirá la descripción de cada problema, el diseño de las entradas y salidas,
las validaciones aplicadas y la explicación del uso de enteros, flotantes y booleanos
como base para la lógica, condiciones y decisiones en cada solución.
"""
### --------------------------------------------------
### 7.1 Problem 1: Temperature converter and range flag
### --------------------------------------------------
"""
Descripción:
Convierte una temperatura en grados Celsius (float) a Fahrenheit y Kelvin. 
Además, determina un valor booleano is_high_temperature que sea true si la temperatura en Celsius es mayor o igual que 30.0 
y false en caso contrario.

Validaciones:
- Verificar que temp_c pueda convertirse a float.
- No permitir temperaturas físicas imposibles en Kelvin (por ejemplo, temp_k < 0.0).
"""
## Operaciones clave sugeridas:
## - Conversión: temp_f = temp_c * 9 / 5 + 32
## - Conversión: temp_k = temp_c + 273.15
## - Comparación: is_high_temperature = (temp_c >= 30.0)

print(f"\n ------------- PROBLEM 1 -------------")
temp_input = input(f"Temperature in C°: ")
temp_c = float(temp_input)
temp_f = (temp_c * 1.8) + 32
temp_k = temp_c + 273.15
    
if temp_c > 30:
    verify_temp = "Hot"
else: 
    verify_temp = "Cold"

if temp_k < 0.0:
    print(f"Impossible physical temperature")
    print(f"Temperature is: {verify_temp}")
else:  
    print(f"Kelvin: {temp_k}")
    print(f"Fahrenheit: {temp_f}")
    print(f"Temperature is: {verify_temp}")
print()
# ------------------------------------------------------------
# CASOS DE PRUEBA (NORMAL, BORDE Y ERROR)
# ------------------------------------------------------------
"""
------------- PROBLEM 1 -------------

Caso 1: NORMAL  
Input:
    Temperature in C°: 25
Output esperado:
    Kelvin: 298.15
    Fahrenheit: 77.0
    Temperature is: Cold


------------- PROBLEM 1 -------------

Caso 2: ERROR (temperatura físicamente imposible → Kelvin < 0)
Input:
    Temperature in C°: -300
Output esperado:
    Impossible physical temperature
    Temperature is: Cold


------------- PROBLEM 1 -------------

Caso 3: BORDE (justo en el límite donde se considera “Hot”: temp_c = 30)
Input:
    Temperature in C°: 30
Output esperado:
    Kelvin: 303.15
    Fahrenheit: 86.0
    Temperature is: Cold
"""
### --------------------------------------------------
### 7.2 Problem 2: Work hours and overtime payment
### --------------------------------------------------
"""
Descripción:
Calcula el pago total semanal de un trabajador. 
Hasta 40 horas se pagan a hourly_rate (float). 
Las horas extra (> 40) se pagan al 150% de la tarifa normal. 
Además, genera un booleano has_overtime que indique si el trabajador hizo horas extra.

Validaciones:
- hours_worked >= 0
- hourly_rate > 0
- Si alguno no cumple, mostrar "Error: invalid input".
"""
## Operaciones clave sugeridas:
## - Uso de min() y max() para separar horas regulares y extra.
## - Cálculo: overtime_pay = overtime_hours * hourly_rate * 1.5
## - Booleano: has_overtime = (hours_worked > 40)

print(f"\n ------------- PROBLEM 2 -------------")
hours_input = input("Hours Worked: ")
rate_input = input("Hourly Rate: ")


hours_worked = float(hours_input)
hourly_rate = float(rate_input)


if hours_worked == 0 or hourly_rate == 0:
    print("Error: invalid input")


regular_hours = min(hours_worked, 40)
overtime_hours = max(0, hours_worked - 40)

regular_pay = regular_hours * hourly_rate
overtime_pay = overtime_hours * hourly_rate * 1.5

total_pay = regular_pay + overtime_pay
has_overtime = overtime_hours > 0

print(f"Regular pay: {regular_pay}")
print(f"Overtime pay: {overtime_pay}")
print(f"Total pay: {total_pay}")
print(f"Has overtime: {has_overtime}")
print()
# ------------------------------------------------------------
# CASOS DE PRUEBA (NORMAL, BORDE Y ERROR)
# ------------------------------------------------------------
"""
------------- PROBLEM 2 -------------

Caso 1: NORMAL (sin horas extra)
Input:
    Hours Worked: 35
    Hourly Rate: 10
Output esperado:
    Regular pay: 350.0
    Overtime pay: 0.0
    Total pay: 350.0
    Has overtime: False


------------- PROBLEM 2 -------------

Caso 2: ERROR (entrada con 0 → inválida)
Input:
    Hours Worked: 0
    Hourly Rate: 15
Output esperado:
    Error: invalid input
    Regular pay: 0.0
    Overtime pay: 0.0
    Total pay: 0.0
    Has overtime: False


------------- PROBLEM 2 -------------

Caso 3: BORDE (justo cuando inicia overtime → 40 horas)
Input:
    Hours Worked: 40
    Hourly Rate: 12
Output esperado:
    Regular pay: 480.0
    Overtime pay: 0.0
    Total pay: 480.0
    Has overtime: False
"""
### --------------------------------------------------
### 7.3 Problem 3: Discount eligibility with booleans
### --------------------------------------------------
"""
Descripción:
Determina si un cliente obtiene un descuento en su compra. La regla es:
- Tiene descuento si:
  - is_student es true OR
  - is_senior es true OR
  - purchase_total >= 1000.0
Calcula también el total a pagar aplicando un 10% de descuento cuando sea elegible.

Validaciones:
- purchase_total >= 0.0
- Normalizar is_student_text e is_senior_text a mayúsculas y convertir a booleanos is_student, is_senior.
- Si el texto no es "YES" ni "NO", mostrar "Error: invalid input".
"""
## Operaciones clave sugeridas:
## - Conversión a bool por comparación de strings.
## - Booleanos: discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
## - Cálculo: final_total = purchase_total * 0.9 si discount_eligible es true, si no, el mismo purchase_total.

print(f"\n ------------- PROBLEM 3 -------------")

purchase_input = input("Purchase Total: ")
student_input = input("Are you a student? (YES/NO): ")
senior_input = input("Are you a senior? (YES/NO): ")
purchase_total = float(purchase_input)
is_student_text = student_input.strip().upper()
is_senior_text = senior_input.strip().upper()
if purchase_total < 0:
    print("Error: invalid input")
    exit()
if is_student_text == "YES":
    is_student = True
elif is_student_text == "NO":
    is_student = False
else:
    print("Error: invalid input")
    exit()
if is_senior_text == "YES":
    is_senior = True
elif is_senior_text == "NO":
    is_senior = False
else:
    print("Error: invalid input")
    exit()
discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
if discount_eligible:
    final_total = purchase_total * 0.9
else:
    final_total = purchase_total

print(f"Discount eligible: {discount_eligible}")
print(f"Final total: {final_total}")
print()
# ------------------------------------------------------------
# CASOS DE PRUEBA (NORMAL, BORDE Y ERROR)
# ------------------------------------------------------------
"""
------------- PROBLEM 3 -------------

Caso 1: NORMAL (descuento por estudiante)
Input:
    Purchase Total: 500
    Are you a student? (YES/NO): YES
    Are you a senior? (YES/NO): NO
Output esperado:
    Discount eligible: True
    Final total: 450.0


------------- PROBLEM 3 -------------

Caso 2: ERROR (entrada inválida → compra negativa)
Input:
    Purchase Total: -100
    Are you a student? (YES/NO): NO
    Are you a senior? (YES/NO): NO
Output esperado:
    Error: invalid input


------------- PROBLEM 3 -------------

Caso 3: BORDE (compra justo en límite de descuento por monto ≥ 1000)
Input:
    Purchase Total: 1000
    Are you a student? (YES/NO): NO
    Are you a senior? (YES/NO): NO
Output esperado:
    Discount eligible: True
    Final total: 900.0
"""
### --------------------------------------------------
### 7.4 Problem 4: Basic statistics of three integers
### --------------------------------------------------
"""
Descripción:
Lee tres números enteros y calcula: suma, promedio (float), valor máximo, 
valor mínimo y un booleano all_even que indique si los tres números son pares

Validaciones:
- Verificar que los tres valores se puedan convertir a int.
- No se requieren restricciones adicionales (se permiten negativos).
"""
## Operaciones clave sugeridas:
## - sum_value = n1 + n2 + n3
## - average_value = sum_value / 3
## - max(), min()
## - all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

print(f"\n ------------- PROBLEM 4 -------------")
num1_input = input("First integer: ")
num2_input = input("Second integer: ")
num3_input = input("Third integer: ")

num1 = int(num1_input)
num2 = int(num2_input)
num3 = int(num3_input)

sum_value = num1 + num2 + num3
average_value = sum_value / 3
max_value = max(num1, num2, num3)
min_value = min(num1, num2, num3)
all_even = (num1 % 2 == 0) and (num2 % 2 == 0) and (num3 % 2 == 0)

print(f"Sum: {sum_value}")
print(f"Average: {average_value}")
print(f"Max: {max_value}")
print(f"Min: {min_value}")
print(f"All even: {all_even}")
print()
# ------------------------------------------------------------
# CASOS DE PRUEBA (NORMAL, BORDE Y ERROR)
# ------------------------------------------------------------
"""
------------- PROBLEM 4 -------------

Caso 1: NORMAL
Input:
    First integer: 4
    Second integer: 6
    Third integer: 8
Output esperado:
    Sum: 18
    Average: 6.0
    Max: 8
    Min: 4
    All even: True


------------- PROBLEM 4 -------------

Caso 2: ERROR (entrada no numérica → genera ValueError)
Input:
    First integer: a
    Second integer: 5
    Third integer: 7
Output esperado:
    (El programa lanzará un error de conversión a int)
    ValueError


------------- PROBLEM 4 -------------

Caso 3: BORDE (mezcla de números pares e impares)
Input:
    First integer: 2
    Second integer: 3
    Third integer: 4
Output esperado:
    Sum: 9
    Average: 3.0
    Max: 4
    Min: 2
    All even: False

"""
### --------------------------------------------------
### 7.5 Problem 5: Loan eligibility (income and debt ratio)
### --------------------------------------------------
"""
Descripción:
Determina si una persona es elegible para un préstamo con base en:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)
La regla es:
- debt_ratio = monthly_debt / monthly_income
- eligible es true si:
  - monthly_income >= 8000.0 AND
  - debt_ratio <= 0.4 AND
  - credit_score >= 650

Validaciones:
- monthly_income > 0.0 (evitar división entre cero).
- monthly_debt >= 0.0
- credit_score >= 0
- Si no se cumple, mostrar "Error: invalid input".
"""
## Operaciones clave sugeridas:
## - Cálculo de deuda relativa: debt_ratio = monthly_debt / monthly_income
## - Booleano: eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)

print(f"\n ------------- PROBLEM 5 -------------")
income_input = input("Monthly Income: ")
debt_input = input("Monthly Debt: ")
score_input = input("Credit Score: ")
monthly_income = float(income_input)
monthly_debt = float(debt_input)
credit_score = int(score_input)
if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
    print("Error: invalid input")
    exit()
debt_ratio = monthly_debt / monthly_income
eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)
print(f"Debt ratio: {debt_ratio}")
print(f"Eligible: {eligible}")
print()
# ------------------------------------------------------------
# CASOS DE PRUEBA (NORMAL, BORDE Y ERROR)
# ------------------------------------------------------------
"""
------------- PROBLEM 5 -------------

Caso 1: NORMAL (cumple requisitos)
Input:
    Monthly Income: 10000
    Monthly Debt: 3000
    Credit Score: 700
Output esperado:
    Debt ratio: 0.3
    Eligible: True


------------- PROBLEM 5 -------------

Caso 2: ERROR (ingreso inválido → negativo)
Input:
    Monthly Income: -5000
    Monthly Debt: 1000
    Credit Score: 700
Output esperado:
    Error: invalid input


------------- PROBLEM 5 -------------

Caso 3: BORDE (justo en los límites)
Input:
    Monthly Income: 8000
    Monthly Debt: 3200
    Credit Score: 650
Output esperado:
    Debt ratio: 0.4
    Eligible: True
"""
### --------------------------------------------------
### 7.6 Problem 6: Body Mass Index (BMI) and category flag
### --------------------------------------------------
"""
Descripción:
Calcula el índice de masa corporal (BMI) de una persona con la fórmula:
- bmi = weight_kg / (height_m * height_m)
Además, genera booleanos para indicar:
- is_underweight (bmi < 18.5)
- is_normal (18.5 <= bmi < 25.0)
- is_overweight (bmi >= 25.0)

Validaciones:
- weight_kg > 0.0
- height_m > 0.0
- Si no se cumple, mostrar "Error: invalid input".
"""
## Operaciones clave sugeridas:
## - Cálculo de bmi como float.
## - Uso de round(bmi, 2) para mostrar 2 decimales.
## - Evaluación de rangos con condiciones encadenadas.

print(f"\n ------------- PROBLEM 6 -------------")
weight_kg = float(input("Peso en kg: "))
height_m = float(input("Estatura en metros: "))

if weight_kg <= 0.0 or height_m <= 0.0:
    print("Error: invalid input")
else:
    
    bmi = weight_kg / (height_m * height_m)
    bmi_rounded = round(bmi, 2)
    is_underweight = bmi < 18.5
    is_normal = 18.5 <= bmi < 25.0
    is_overweight = bmi >= 25.0

    print("BMI:", bmi_rounded)
    print("Underweight:", str(is_underweight).lower())
    print("Normal:", str(is_normal).lower())
    print("Overweight:", str(is_overweight).lower())
print()
# ------------------------------------------------------------
# CASOS DE PRUEBA (NORMAL, BORDE Y ERROR)
# ------------------------------------------------------------
"""
------------- PROBLEM 6 -------------

Caso 1: NORMAL (IMC dentro del rango normal)
Input:
    Peso en kg: 70
    Estatura en metros: 1.75
Output esperado:
    BMI: 22.86
    Underweight: false
    Normal: true
    Overweight: false


------------- PROBLEM 6 -------------

Caso 2: ERROR (peso negativo)
Input:
    Peso en kg: -60
    Estatura en metros: 1.7
Output esperado:
    Error: invalid input


------------- PROBLEM 6 -------------

Caso 3: BORDE (IMC justo en límite bajo de normal → 18.5)
Input:
    Peso en kg: 57
    Estatura en metros: 1.75
Output esperado:
    BMI: 18.61
    Underweight: false
    Normal: true
    Overweight: false
"""
# -------------------------------------------------------------------------
#### CONCLUSIONES
"""
Los enteros y flotantes suelen combinarse para representar cálculos reales, como horas, precios o promedios.
Las comparaciones producen valores booleanos que permiten decidir rutas de ejecución mediante if y estructuras similares.
Validar rangos y evitar divisiones entre cero es clave para prevenir errores lógicos y fallas en tiempo de ejecución.
También aprendí que las condiciones compuestas con and, or y not permiten controlar casos más específicos y complejos.
Estos mismos patrones se repiten constantemente en problemas de nómina, descuentos, préstamos y muchos otros cálculos reales.
"""
#### REFERENCIAS
"""
# 1) Python documentation - Numeric Types: int, float, complex (Built-in Types) — documentación oficial de tipos numéricos   
# 2) Python documentation - Boolean type: bool — cómo Python maneja valores booleanos y su relación con int 
# 3) Tutorial sobre operadores aritméticos, relacionales y lógicos en Python — operadores +, -, *, /, ==, >, and, or, not   
# 4) Introducción a tipos y variables en Python — artículo explicando int, float, bool y conversiones entre ellos  
# 5) Apuntes de programación básica (curso universitario) explicando tipos numéricos y su uso en algoritmos fundamentales 
"""


