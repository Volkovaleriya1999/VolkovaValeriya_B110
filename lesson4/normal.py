# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(m, n):
    fibonacci_list = [1, 1]
    gold_list = [] #золотое сечение
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fnumSum = fib1 + fib2
        gold = fib2 / fib1
        gold = round(gold, 3)
        gold_list.append(gold)
        fibonacci_list.append(fnumSum)
        fib1 = fib2
        fib2 = fnumSum
        i += 1
    print(fibonacci_list[m:n], '\n', gold_list[m:n])

fibonacci(4, 20)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(len(origin_list)):
        for j in range(i + 1, len(origin_list)):
            if origin_list[i] > origin_list[j]:
                origin_list[i], origin_list[j] = origin_list[j], origin_list[i]
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


years = [1994, 1982, 1798, 1865, 1500, 1999, 2010, 2018, 1972]

def key(years):
    return years > 1850

def my_filter(func, lst):
    i = 0
    while i < len(lst):
        if func(lst[i]):
            pass
        else:
            lst.pop(i)
            i -= 1
        i += 1
    return lst

print(my_filter(key, sort_to_max(years)))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

x1, y1 = [2, 5]
x2, y2 = [1, 4]
x3, y3 = [6, 6]
x4, y4 = [7, 3]

def parallelogramm(x1, y1, x2, y2, x3, y3, x4, y4):
    if x1 is int and y1 is int and x2 is int and y2 is int and x3 is int and y3 is int and x4 is int and y4 is int:
        if (x1 + x3 == x2 + x4) and (y1 + y3 == y2 + y4): # or (x1 - x3 == x2 - x4) and (y1 - y3 == y2 - y4):
            return True
        else:
            return False
    else:
        return False

#       НЕ РАБОТАЕТ, НО Я ПЫТАЛАСЬ)))))))

print(parallelogramm(x1, y1, x2, y2, x3, y3, x4, y4))

