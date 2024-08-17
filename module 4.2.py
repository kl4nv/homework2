class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            return print('Такого этажа нет')


info = House('ЖК Полюса', 25)
info.go_to(3)
info1 = House('ЖК Космос', 45)
info1.go_to(50)
