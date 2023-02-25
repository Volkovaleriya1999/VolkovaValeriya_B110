# Задача:
# Напишите небольшую консольную утилиту, позволяющую работать с папками и файлами.
# Утилита должна работать с помощью параметров и флагов, передаваемых скрипту в командной строке.
# Примеры:
#     python hw06_hard.py -touch ../dir1/test.txt -ls ../dir1/
#     python hw06_hard.py -rm ../dir1/test.txt -ls ../dir1/
#     python hw06_hard.py -mkdir ../dir1/newdir -ls ../dir1/
#     python hw06_hard.py -ls ../dir1/
#     python hw06_hard.py -touch ../dir1/test.txt
#
#     и.т.д.
#
# Используйте модули argparse (для разбора аргументов), os, sys.
#
# Утилита должна принимать следующие флаги и выполнять следующие действия:
# "-ls <путь до папки>" - Посмотреть все файлы и подпапки в папке
# "-touch <путь до нового файла>" - Создать файл
# "-rm <путь до файла>" - Удалить файл
# "-mkdir <путь до папки>" - Создать папку
#
# Каждый из представленных параметров не обязательный, но если не указать никакой, то утилита должна вывести
# уведомление, которая предлагает посмотреть --help.
# Предусмотреть обработку исключений, например, если пытаются посмотреть все файлы не у папки, а у файла и.т.д.
# """


import os
import  argparse


def make_file(file_name):
    if file_name:
        try:
            text_file = open(file_name, "w")
        except FileExistsError:
            print(f'Файл {file_name} уже создан')


def remove_file(file_name):
    if file_name:
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print(f'Файл {file_name} уже удален.')


def make_dir(dir_name):
    if dir_name:
        try:
            os.mkdir(dir_name)
            print(f'Директория {dir_name} создана.')
        except FileExistsError:
            print(f'{dir_name}')


def view_directory(my_directory):
    my_directory = os.listdir()
    for i in my_directory:
        print(i)



def create_parser():
    parser = argparse.ArgumentParser(description='Работа с папками и файлами.')
    parser.add_argument('--ls', metavar='ls', type=str, help='посмотреть все файлы и подпапки в папке')
    parser.add_argument('--touch', metavar='touch', type=str, help='создать файл.')
    parser.add_argument('--mkdir', metavar='mkdir', type=str, help='создать папку.')
    parser.add_argument('--rm', metavar='rm', type=str, help='удалить файл.')

    return parser


if __name__ == '__main__':

    parser = create_parser()
    args = parser.parse_args()


    if args.mkdir:
        make_dir(args.mkdir)

    elif args.touch:
        make_file(args.touch)

    elif args.ls:
        view_directory(args.ls)

    elif args.rm:
        remove_file(args.rm)


##   В ЦЕЛОМ РАБОТАЕТ (ЕЛЕ КАК) И НЕМНОГО РАЗОБРАЛАСЬ, НО МНОГОЕ ДО СИХ ПОР ОСТАЕТСЯ ЗАГАДКОЙ...............))1)

