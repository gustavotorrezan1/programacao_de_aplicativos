valores = []
for y in range(1, 5):
        valores.append(int(input(f'Digite um valor de 0 a 10= {y}:')))
soma = 0
for i in valores:
   soma += i
soma_valores = soma

media_valores = soma_valores / 4

print(f'A média é: {media_valores}')

if media_valores >=7:
    print('Se a média é  acima de 7 = Aprovado')
else:
    print('Se a média é  abaixo de 7 = Reprovado')