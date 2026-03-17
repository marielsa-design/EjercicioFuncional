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
# Pedir horas trabajadas
# Pedir valor por hora
# Llamar a la función
# Mostrar el salario final.

def calcular_salario(horas, valor_hora):
    if horas <= 40:
        salario = horas * valor_hora
    else:
        horas_normales = 40
        horas_extras = horas - 40
        salario = (horas_normales * valor_hora) + (horas_extras * valor_hora * 2)
        return salario
    
nombre = input("Ingrese tu nombre del empleado: ")

horas = float(input("Ingrese las horas trabajadas: "))

valor_hora = float(input("Ingrese el valor por hora: "))

salario_total = calcular_salario(horas, valor_hora)

print(f"{nombre}, su salario totales es: ${salario_total}")