preco = float(input('Digite o valor da compra: '))
dinheiro = float(input('Digite a quantia de dinheiro entregue: '))
troco = dinheiro - preco
totalNota = 0
i = 0
n = [200, 100, 50, 20, 10, 5, 2]
c = [1, 0.50, 0.25, 0.10, 0.5, 0.01]
while True:
    if troco >= n[i]:
        troco -= n[i]
        totalNota += 1
    else:
        if totalNota > 0:
            print(f'Total de {totalNota} notas de R${n[i]}')
        if n[i] == n[i]:
            i += 1
        if i == 5 or troco == 0:
            break
i = 0
totalNota = 0
if troco < 2:
    while True:
        if troco >= c[i]:
            troco -= c[i]
            totalNota += 1
        else:
            if totalNota > 0:
                print(f'Total de {totalNota} moedas de R${c[i]}')
            if c[i] == c[i]:
                i += 1
            if i == 5 or troco <= 0.009:
                break

