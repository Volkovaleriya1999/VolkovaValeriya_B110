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
#
#
# # Задача-2:
# # Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# # из которой запущен данный скрипт.
# # И второй скрипт, удаляющий эти папки.
#
import os
#
# def make_dir():
#     try:
#         for i in range(1, 10):
#             os.mkdir("dir_" + str(i))
#     except FileExistsError:
#         print('Файл уже создан')
#
#
# def remove_dir():
#     try:
#         for i in range(1, 10):
#             os.rmdir("dir_" + str(i))
#     except FileNotFoundError:
#         print('Файл уже удален')
#
#
# if __name__ == '__main__':
#     make_dir()
#     remove_dir()
#
#
#
# # Задача-3:
# # Напишите скрипт, отображающий папки текущей директории.
#
# def view_directory():
#     my_directory = os.listdir()
#     for i in my_directory:
#         print(i)
#
#
# # Задача-4:
# # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
#
#
# import shutil
#
#
# if __name__ == '__main__':
#     shutil.copy(__file__, 'my_copy_file.py')
#
