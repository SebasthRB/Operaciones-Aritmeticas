def MaximoComunDivisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("CALCULADORA DE MÁXIMO COMÚN DIVISOR")

# Solicitar al usuario ingresar el primer número
while True:
    try:
        num1 = int(input("Ingresa el primer número: "))
        if num1 > 0:
            break
        else:
            print("Por favor, ingresa un número positivo.")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

# Solicitar al usuario ingresar el segundo número
while True:
    try:
        num2 = int(input("Ingresa el segundo número: "))
        if num2 > 0:
            break
        else:
            print("Por favor, ingresa un número positivo.")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

resultado = MaximoComunDivisor(num1, num2)
print("El Máximo Común Divisor de", num1, "y", num2, "es:", resultado)
