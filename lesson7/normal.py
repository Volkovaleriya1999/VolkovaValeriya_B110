# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.



# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


# class School:
#     def __init__(self, teachers, classes):
#         self.teachers = teachers
#         self.classes = classes
#
#     def get_stedents(self):
#         return f'Список классов:\n{self.classes}'
#
#     def get_teachers(self):
#         return f'Список учителей: {self.teachers}'
#
#
# class Class:
#     def __init__(self, name, students):
#         self.name = name
#         self.students = students
#
#     def get_students_in_class(self):
#         return f'Класс: {self.name}, ученики: {self.students}'
#
#
# class Person:
#     def __init__(self, first_name, last_name, middle_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.middle_name = middle_name
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name} {self.middle_name}'
#
#
# class Student(Person):
#     def __init__(self, first_name, last_name, middle_name,
#                  class_room, mother, father):
#         super().__init__(first_name, last_name, middle_name)
#         self._class_room = class_room
#         self._parents = {
#             'mother': mother,
#             'father': father
#         }
#
#     def get_parents(self):
#         return f'Ученик: {self.last_name}, мама: {self._parents[0]} папа: {self._parents[1]}'
#
#
# class Teacher(Person):
#     def __init__(self, first_name, last_name, middle_name, subject):
#         super().__init__(first_name, last_name, middle_name)
#         self.subject = subject
#

# # ПОКА НЕ ДОДЕЛАЛА
