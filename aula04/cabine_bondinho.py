print('Cabine do Bondinho')

alunos = int(input('Entre com a quantidade de alunos: '))
monitores = int(input('Entre com a quantidade de monitores: '))

total = alunos + monitores

if total > 50:
    print(f'O total de pessoas na cabine é de {total}')
    print(f'Não será possível levar {alunos} alunos e {monitores} monitores duma só vez')
else:
    print(f'O total de pessoas na cabine é de {total}')
    print(f'Capacidade aceitável.')