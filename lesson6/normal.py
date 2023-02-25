# # Задача-1:
# # Следующая программа написана верно, однако содержит места потенциальных ошибок.
# # используя конструкцию try добавьте в код обработку соответствующих исключений.
# # Пример.
# # Исходная программа:
#
# def avg(a, b):
#     if a * b >= 0:
#         return (a * b) ** 0.5
#     else:
#         raise ValueError('Невозможно найти среднее геометрическое этих чисел')
#
#
# try:
#     a = float(input("a = "))
#     b = float(input("b = "))
#     c = avg(a, b)
#     print("Среднее геометрическое = {:.2f}".format(c))
# except ValueError:
#     print('Проверьте введенные числа!')
# except Exception as e:
#     print('Ошибка: ', e)

# Задача-2:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь "меню" выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


# import os
# import sys
# from easy import view_directory
#
# #
# print('sys.argv = ', sys.argv)


# def print_help():
#     print('help - получение справки')
#     print('chdir <dir_name> - перейти в папку')
#     print('listdir <dir_name> - просмотреть содержимое текущей папки')
#     print('rmdir <dir_name> - удалить папку')
#     print('mkdir <dir_name> - создать папку')
#
#
# def change_dir():
#     dir_name = sys.argv[2]
#     if dir_name:
#         try:
#             os.chdir(dir_name)
#             print(f'Вы успешно перешли в директорию {dir_name}', os.getcwd())
#         except FileNotFoundError:
#             print(f'Папки {dir_name} не существует!')

# def make_dir():
#     dir_name = sys.argv[2]
#     if dir_name:
#         try:
#             os.mkdir(dir_name)
#             print(f'Директория {dir_name} создана.')
#         except FileExistsError:
#             print(f'{dir_name}')

#
# def remove_dir():
#     dir_name = sys.argv[2]
#     if dir_name:
#         try:
#             os.rmdir(dir_name)
#             print(f'Директория {dir_name} удалена.')
#         except FileNotFoundError:
#             print(f'Директория {dir_name} уже удалена.')


# action_dict = {
#     'help': print_help,
#     'chdir': change_dir,
#     'listdir': view_directory,
#     'mkdir': make_dir,
#     'rmdir': remove_dir
# }
#
# try:
#     dir_name = sys.argv[2]
# except IndexError:
#     dir_name = None
#
# try:
#     key = sys.argv[1]
# except KeyError:
#     key = None
#
#
# func_to_do = action_dict.get(key, action_dict['help'])
# func_to_do()


