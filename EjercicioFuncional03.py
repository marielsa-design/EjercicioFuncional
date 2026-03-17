# Sistema simple de cálculo de salario

# Una empresa paga a sus empleados según las horas trabajadas.

# Debes crear una función llamada:
# calcular_salario(horas, valor_hora)

# Reglas:

# Si trabaja hasta 40 horas, se paga normal
# Si trabaja más de 40 horas, las horas extra se pagan al doble

# La función debe:

# Calcular el salario total
# Retornar el resultado

# El programa principal debe:

# Pedir el nombre del empleado

nombre = input("Ingrese tu nombre del empleado: ")

# Pedir horas trabajadas

horas = float(input("Ingrese las horas trabajadas: "))

# Pedir valor por hora

valor_hora = float(input("Ingrese el valor por hora: "))

# Llamar a la función

def calcular_salario(horas, valor_hora):
    if horas <= 40:
        salario = horas * valor_hora
    else:
        horas_normales = 40
        horas_extras = horas - 40
        salario = (horas_normales * valor_hora) + (horas_extras * valor_hora * 2)
        return salario

salario_total = calcular_salario(horas, valor_hora)

# Mostrar el salario final.

print(f"{nombre}, su salario totales es: ${salario_total}")