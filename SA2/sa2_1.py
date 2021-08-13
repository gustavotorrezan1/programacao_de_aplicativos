list = [5, 7, 2, 9, 4, 1, 3]

def total_elementos(list):
    count = 0
    for element in list:
        count += 1
    return count

#print(total_elementos(list))
i = 0
maior = list[1]
while(i <= total_elementos(list)):
    if list[i + 1] > list[i]:
        maior = list[i+1]



print(maior)
