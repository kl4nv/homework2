my_dict = {'Kirill': 12345, 'Mark':777777, "Lena":565656}
print(my_dict)
print(my_dict['Kirill'])
print(my_dict.get('vvv'))
my_dict['Bob'] = 65983
my_dict['Karl'] = 239856
del my_dict['Mark']
print(my_dict)
my_set = {8, 2.5, 'kkk', 8, True, 2, 2.5}
print(my_set)
my_set.update({55,9})
print(my_set)
my_set.discard(True)
print(my_set)
