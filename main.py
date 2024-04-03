def MaximoComunDivisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solicitar_numero(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if num > 0:
                return num
            else:
                print("Por favor, ingresa un número positivo.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

print("CALCULADORA DE MÁXIMO COMÚN DIVISOR")

num1 = solicitar_numero("Ingresa el primer número: ")
num2 = solicitar_numero("Ingresa el segundo número: ")

resultado = MaximoComunDivisor(num1, num2)
print("El Máximo Común Divisor de", num1, "y", num2, "es:", resultado)