# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random


list1 = [random.randint(1, 10) for _ in range(10)]
list2 = [i ** 2 for i in list1]
print('list1 - ', list1)
print('list2 - ', list2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_list1 = ['яблоко', 'банан', 'апельсин', 'папайя', 'манго']
fruit_list2 = ['яблоко', 'гранат', 'киви', 'мандарин', 'манго']
fruit_list3 = [i for i in fruit_list1 if i in fruit_list2]
print(fruit_list3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random


list1 = [random.randint(-100, 100) for _ in range(10)]
list2 = [i for i in list1 if i % 3 == 0 if i > 0 if i % 4 > 0]
print(list1)
print(list2)