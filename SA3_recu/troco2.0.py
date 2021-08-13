print('CALCULE O TROCO')
compras = float(input('Qual foi o valor das compras?'))
dinheiro = float(input('Qual o valor em dinheiro?'))
valor = round((dinheiro - compras), 2)
print(f'Seu troco é de R$ {valor} em notas de:')
total = valor
print('-' * 100)
notas = 100
totalNotas = 0
while True:
    if total >= notas:
        total -= notas
        totalNotas += 1
    else:
        if compras == dinheiro:
            print("NÃO TEM TROCO")
        if totalNotas > 0:
            print(f'{totalNotas} cédulas de R${notas}')
        if notas == 100:
            notas = 50
        elif notas == 50:
            notas = 20
        elif notas == 20:
            notas = 10
        elif notas == 10:
            notas = 5
        elif notas == 5:
            notas = 2
        elif notas == 2:
            notas = 1
        elif notas == 1:
            notas = 0.5
        elif notas == 0.5:
            notas = 0.25
        elif notas == 0.25:
            notas = 0.10
        elif notas == 0.10:
            notas = 0.05
        elif notas == 0.05:
            notas = 0.01
        elif notas == 0.01:
            notas = 1
        totalNotas = 0
        if total == 0:
            break


