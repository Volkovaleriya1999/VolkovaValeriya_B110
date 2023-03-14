# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


class Worker:
    def __init__(self, name, surname, salary, norm_hours):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.norm_hours = norm_hours
        self.fact_hours = 0


    def number_of_hours(self):
        with open('hours.txt', 'r') as f:
            for i in f.readlines():
                if i.split()[0] == self.name and i.split()[1] == self.surname:
                    self.fact_hours = int(i.split()[2])
                    break
                else:
                    continue

    def calc_salary(self):
        one_hour = self.salary // self.norm_hours
        salary = 0


# # ПОКА НЕ ДОДЕЛАЛА
