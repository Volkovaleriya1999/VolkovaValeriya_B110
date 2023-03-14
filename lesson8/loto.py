"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""


# # Вспомнила, что как-то делала что-то связанное с лото

import random
#

# def random_loto_card():
#     rand_nums_1_15 = [x for x in range(1, 15)]
#     rand_nums_16_30 = [x for x in range(16, 30)]
#     rand_nums_31_45 = [x for x in range(31, 45)]
#     rand_nums_46_60 = [x for x in range(46, 60)]
#     rand_nums_61_75 = [x for x in range(61, 75)]
#
#     loto_card = {
#         'B': random.sample(rand_nums_1_15, k=5),
#         'I': random.sample(rand_nums_16_30, k=5),
#         'N': random.sample(rand_nums_31_45, k=5),
#         'G': random.sample(rand_nums_46_60, k=5),
#         'O': random.sample(rand_nums_61_75, k=5)
#     }
#
#     return loto_card
#
#
# def front_loto_card(loto_card):
#     print('_' * 26)
#     for logo in loto_card.keys():
#         print("| ", logo, end=' ')
#     print('|')
#     print('-' * 26)
#
#     for i in range(5):
#         print(end='')
#         for values in loto_card.values():
#             if len(str(values[i])) == 2:
#                 print("|", values[i], end=' ')
#             else:
#                 print("|", values[i], end='  ')
#         print('|')
#     print('-' * 26)
#
#
# card = random_loto_card()
# front_loto_card(card)





# class Card:
#     def __init__(self):
#         self.temp = []
#
#     def lines(self, temp):
#         nums = []
#         while len(nums) < 5:
#             elem = str(random.randint(1, 90))
#             if elem not in temp:
#                 nums.append(elem)
#                 temp.append(elem)
#         nums = list(nums) + list(' ' * 4)
#         random.shuffle(nums)
#         return ' '.join(nums)
#
#     def result_card(self):
#         print('-' * 22)
#         for i in range(3):
#             print(self.lines(self.temp))
#         print('-' * 22)
#
#
#
# class Barrel:
#     num = None
#
#     def __init__(self):
#         self.num = random.randint(1, 90)
#
#     def __str__(self):
#         return {self.num}
#
#     @property
#     def barrel_num(self):
#         return self.num
#
#
#
# def generate_barrels(count, min, max):
#     barrels_list = []
#     while len(barrels_list) < count:
#         barrel = random.randint(min, max)
#         if barrel not in barrels_list:
#             barrels_list.append(barrel)
#     return barrels_list
#
#
# class Game:
#     number_of_barrels = 90
#     usercard = Card()
#     computercard = Card()
#     barrels = []
#     game_over = False
#
#     def __init__(self):
#         self.usercard = self.usercard.result_card()
#         self.computercard = self.computercard.result_card()
#         self.barrels = generate_barrels(self.number_of_barrels, 1, 90)
#
#     def play(self):
#         barrel = self.barrels.pop()
#         print(f'Бочонок №{barrel}. Осталось {len(self.barrels)}')
#         print(f'---- Ваша карточка ---\n{self.usercard}')
#         print(f'- Карточка компьютера-\n{self.computercard}')
#
#         useranswer = input('Зачеркнуть цифру? (y/n)').lower().strip()
#         if useranswer == 'y' and not barrel in self.usercard or \
#            useranswer != 'y' and barrel in self.usercard:
#             return 'computer wins'
#
#
#
# if __name__ == '__main__':
#     game = Game()
#     score = game.play()











