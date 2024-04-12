# Este código tenta implementar um jogo simples de adivinhação de números.
# O programa deve escolher um número aleatório entre 1 e 10 e permitir que o usuário tente adivinhar o número.
# No entanto, o código está incompleto e contém erros.
# Complete e corrija o código para que o jogo funcione corretamente.
# O usuário tem três tentativas para adivinhar o número. Após cada tentativa, o programa deve informar
# se o palpite é muito alto, muito baixo ou correto.

import random

numero_secreto = random.randint(1,10)
tentativas = 3

while tentativas > 0:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    if palpite == numero_secreto:
        print("Parabéns! Seu palpite está correto.")
        break
    elif palpite < numero_secreto:
        print("Seu palpite é muito baixo.")
    else:
        print("Seu palpite é muito alto.")
    tentativas -= 1

if tentativas == 0:
    print("Suas tentativas acabaram. ")
    print("O número secreto era:", numero_secreto)

print("Fim do jogo.")