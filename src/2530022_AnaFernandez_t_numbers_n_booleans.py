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

print()
print(f"Regular pay: {regular_pay}")
print(f"Overtime pay: {overtime_pay}")
print(f"Total pay: {total_pay}")
print(f"Has overtime: {has_overtime}")















