listanum = []
maiorn = 0
menorn = 0
for y in range(0, 20):
        listanum.append(int(input(f'Digite um valor para a Posição {y}:')))
        if y == 0:
            maiorn = menorn = listanum[y]
        else:
            if listanum[y] > maiorn:
                maiorn = listanum[y]
            if listanum[y] < menorn:
                menorn = listanum[y]

media = sum(listanum)/len(listanum)

print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi: {maiorn}')
print(f'O menor valor digitado foi: {menorn}')
print(f'A média dos valores digitados foi: {media}')