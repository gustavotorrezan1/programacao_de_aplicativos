#1
L = [5, 7, 2, 9, 4, 1, 3]
def total_elementos(L):
    count = 0
    for element in L:
        count += 1
    return count
print("tamanho da lista é", total_elementos(L))

#2
print("o maior número é", max(L))

#3
print("o menor número é", min(L))

#4
soma = 0
for i in L:
   soma += i
print("A soma dos elementos da lista é: ", soma)

#5
print('decrecente', sorted(L))

#6
print('crescente', sorted(L, reverse = True))