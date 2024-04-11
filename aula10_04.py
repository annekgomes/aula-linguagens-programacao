# Faça um programa em Python que receba 10 notas do usuario
# guarde em uma lista e tire a média dessas notas
# no final o programa deve imprimir se o aluno foi aprovado
# ou nao, considerando que a media é 7.

notas = []
i = 1

nota = float(input('nota[0]:'))

while nota != -1:
    notas.append(nota)
    nota = float(input('nota['+str(i)+']:'))
    i += 1

media = sum (notas) / len(notas)

if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')

