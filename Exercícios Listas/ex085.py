todos = [[], []]
num = 0
for x in range(1, 8):
    num = int(input(f'Digite o {x}° número: '))
    if num % 2 == 0:
        todos[0].append(num)
    else:
        todos[1].append(num)

todos[0].sort()
todos[1].sort()

print(f'Estes são os valores pares em ordem crescente = {todos[0]}')
print(f'Estes são os valores impares na ordem crescente = {todos[1]}')
