# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle:
    def __init__(self, x1, y1, x2, y2 , x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def calculate_area(self):
        self.area = math.fabs((self.x2 - self.x1) * (self.y3 - self.y1) - (self.x3 - self.x1) * (self.y2 - self.y1)) / 2

        return f'Площадь треугольника равна {self.area}'


    def calculate_height(self):
        side = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** (1 / 2)
        height = 2 * self.area / side

        return f'Высота треугольника равна {round(height, 3)}'


    def calculate_perimeter(self):
        side1 = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** (1 / 2)
        side2 = ((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2) ** (1 / 2)
        side3 = ((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2) ** (1 / 2)

        perimeter = side1 + side2 + side3

        return f'Периметр треугольника равен {round(perimeter, 3)}'


my_triangle = Triangle(1, 5, 2, 3, 6, 4)
print(my_triangle.calculate_area())
print(my_triangle.calculate_height())
print(my_triangle.calculate_perimeter())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


