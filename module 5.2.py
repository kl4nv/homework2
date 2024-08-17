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

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name} Кол-во этажей: {self.number_of_floors}'


info1 = House('ЖК Полюса', 25)
info2 = House('ЖК Космос', 45)

print(info1)
print(len(info1))



