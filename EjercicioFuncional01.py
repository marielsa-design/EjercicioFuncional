# Ejercicio 1 — Fácil
# Determinar si un número es positivo, negativo o cero

# Crea una función llamada:

# analizar_numero(numero)

# La función debe:

# Recibir un número

# Determinar si el número es:

# positivo

# negativo

# cero

# Retornar un mensaje con el resultado.

# El programa principal debe:
 
# Mostrar el resultado

def analizar_numero(): 
    numero = int(input("Ingresar un numero: ")) # Pedir al usuario que ingrese un número.
    if numero < 0:
        print(f"Negativo") 
        return
    
    if numero > 0:
        print(f"Positvo")
        return
    
    if numero == 0:
        print(f"Cero")
        return

analizar_numero() # Llamar a la función analizar_numero.