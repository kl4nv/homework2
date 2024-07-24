def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(4, 2, 3)
print_params()
print_params(3, 2)
print_params(b = 25) # Работает заменяет b на 25, другие параметры берутся из функции
print_params(c = [1, 2, 3]) # Работает заменяет c на список, другие параметры берутся из функции

values_list = [True, 2, (55, 66, 77)]
values_dict = {'a': 1, 'b': 'строка', 'c': True}

print_params(*values_list)
print_params(**values_dict) # Ключи словаря соответствуют переменным из print_params, иначе была бы ошибка

values_list_2 = [5, False]
print_params(*values_list_2, 42) # Работает, потому что 2 элемента списка назначаются на а и b
                                    # и еще 1(с) переназначаем в print_params
