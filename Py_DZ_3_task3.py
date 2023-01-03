#  3.Задайте список из вещественных чисел. 
#  Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#  Пример:   - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = list(map(float, input('Введите список чисел через пробел:').split()))
print(my_list)
if len(my_list) == 0:
    print('Значение NULL, введен пустой список')
elif len(my_list) == 1:
    print(0)
else:    
    differance = i = 0
    max = min = my_list[0] % 1
    for i in my_list:
        if i % 1 == 0:
            continue
        if i % 1 > max:
            max = i % 1 
        if i % 1 < min:
            min = i % 1             
    differance = round(max - min, 4)
    print(differance)        
