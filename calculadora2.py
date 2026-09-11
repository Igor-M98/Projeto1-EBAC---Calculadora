# Solicitar que o usuário informe seus números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operaçao = input("Digite a operação (+, -, *, /): ")

# Condicional para obter o tipo de operação aritmética que o usuário deseja realizar
if operaçao == "+":
    resultado = numero1 + numero2
    print(f"O resultado da soma é: {resultado}")
elif operaçao == "-":
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
elif operaçao == "*":
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
elif operaçao == "/":
    resultado = numero1 / numero2
    print(f"O resultado da divisão é: {resultado}")
else:
    print("Operação inválida")
