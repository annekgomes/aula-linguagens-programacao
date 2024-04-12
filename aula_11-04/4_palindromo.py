# O código abaixo é uma tentativa de criar um verificador de palíndromos.
# Palíndromos são palavras ou frases que são iguais quando lidas de trás para frente.
# No entanto, o código está incompleto e contém erros.
# Complete e corrija o código para que ele funcione corretamente.
# O usuário deve digitar uma palavra ou frase, e o programa deve imprimir se é um palíndromo ou não.
# Ignore espaços, pontuações e diferenças entre maiúsculas e minúsculas.

texto = input("Digite um texto: ")

texto_processado = ''.join(c.lower() for c in texto if c.isalnum())

texto_invertido = texto_processado[::-1]

if texto_processado == texto_invertido:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
