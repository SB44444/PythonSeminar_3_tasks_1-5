
#  2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#  Пример:
#  - [2, 3, 4, 5, 6] => [12, 15, 16];
#  - [2, 3, 5, 6] => [12, 15]

my_list = list(map(int, input('Введите список чисел через пробел:').split())) 
print(my_list)
if len(my_list) == 0:
    print('Сумма: NULL, введен пустой список')
elif len(my_list) == 1:
    print(my_list[0])
else:    
    sum = 0
    i = 0
    j = len(my_list)
    k = int(len(my_list)/2)
    while i < int(len(my_list) / 2):
        j -= 1
        sum = my_list[i] * my_list[j]
        i += 1
        print(sum, end= '; ')
