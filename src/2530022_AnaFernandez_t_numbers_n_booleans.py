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

### ---------------------------------------------
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



