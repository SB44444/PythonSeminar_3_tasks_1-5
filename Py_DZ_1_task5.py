#  5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#  Пример:
#  - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

num = int(input('Введите число элемнтов последовательности Фибоначчи больше 2: '))
n1, n2 = 1, 1
fibonachi_Plus = []
for i in range(num):
    fibonachi_Plus.append(n1) # Добавляются элементы согласно формуле последовательности в положительный список 
    n1, n2 = n2, (n2 + n1)
n1, n2 = 0, 1
fibonachi_Mius = []
for i in range(num + 1):
    fibonachi_Mius.insert(0, n1)  # Добавляются элементы согласно формуле последовательности в отрицательный список 
    n1, n2 = n2, (n1 - n2)
fibonachi_Mius += fibonachi_Plus  # Складываются списки в итоговый
print(*fibonachi_Mius)     
