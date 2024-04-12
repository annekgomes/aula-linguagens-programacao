# O código abaixo tem alguns problemas e está incompleto!
# Altere o código abaixo para que ele atue como uma calculadora
# O usuário deve digitar um valor, um operador e outro valor
# seu programa deverá imprimir na tela o resultado da operação
# Faça com que o seu programa funcione até que o usuário digite -1

valor1 = int(input("Digite um valor: "))

if valor1 == -1:
    print("Programa Encerrado")
else:
    operador = input("Digite um operador matemático para realizar uma operação (+, -, *, /): ")
    valor2 = int(input("Digite outro valor: "))

    if valor2 == -1:
        print("Programa Encerrado")
    else:
        resultado = 0

        if operador == '+':
            resultado = valor1 + valor2
        elif operador == '-':
            resultado = valor1 - valor2
        elif operador == '*':
            resultado = valor1 * valor2
        elif operador == '/':
            resultado = valor1 / valor2
        else:
            print('Operador inválido')

        print(resultado)