#      1/Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#  Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = list(map(int, input('Введите список чисел через пробел:').split())) 
print(my_list)
count = 0
for i in range(2, len(my_list), 2): # Для нечетных позиций по списку, нужно начать с i == 0
   count += my_list[i]
print(f'Сумма чисел, находящихся на нечетной позиции по индексу в списке составила: {count}') # Как в примере