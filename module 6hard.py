import math
class Figure:
    sides_count = 0
    def __init__(self, __color, *__sides):
        if self.__is_valid_color(__color[0], __color[1], __color[2]):
            self.__color = __color
        else:
            print(f'Цвета {__color} не существует')
        self.__sides = [1] * self.sides_count
        self.set_sides(*__sides)
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        count = 0
        for i in [r, g, b]:
            if 0 <= i <= 255:
                count += 1
        if count == 3:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
            self.filled = True

    def __is_valid_size(self, *__sides):
        count = 0
        for i in __sides:
            if isinstance(i, int) and i > 0:
                count += 1
        if count == len([__sides]):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        if isinstance(self.__sides, int):
            return self.__sides
        else:
            return sum(self.__sides)

    def set_sides(self, *new_sides):
        list_sides = []
        for i in new_sides:
            if self.__is_valid_size(i):
                list_sides += [i]
        if len(list_sides) == self.sides_count:
            self.__sides = list_sides
        elif len(list_sides) == 1:
            self.__sides = self.sides_count * list_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides):
        Figure.__init__(self, __color, *__sides)
        self.__radius = self.get_radius()

    def get_square(self):
        return print(math.pi * self.__radius * 2)

    def get_radius(self):
        self.__radius = self.__len__() / (2 * math.pi)
        return self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides):
        if len(__sides) == 3:
            if (__sides[0] > __sides[1] + __sides[2]  # Сторона тр-ка должна быть меньше суммы двух других
                    or __sides[1] > __sides[0] + __sides[2]
                    or __sides[2] > __sides[1] + __sides[0]):
                Figure.__init__(self, __color, 1)
            else:
                Figure.__init__(self, __color, *__sides)
        self.__square = self.get_square()

    def get_square(self):
        li_ = self._Figure__sides
        p = 0.5 * self.__len__()
        S_Triangle = math.sqrt(p * (p - li_[0]) * (p - li_[1]) * (p - li_[2]))
        return S_Triangle


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides):
        if __sides.count(__sides[0]) != len(__sides):    # стороны куба должны быть одинаковы
            Figure.__init__(self, __color, 1)    # иначе принимаем сторону куба как 1
        else:
            Figure.__init__(self, __color, *__sides)
        self.__volume = self.get_volume()

    def get_volume(self):
        V_cube = self._Figure__sides[0] ** 3
        return V_cube


circle1 = Circle((200, 200, 100), 20) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((143,234,10), 3, 4, 6)


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(3, 1, 2) # Не изменится
print(cube1.get_sides())
circle1.set_sides(10) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
