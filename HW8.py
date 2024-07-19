my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(my_list) and my_list[a] >= 0:
    if my_list[a] == 0:
        a += 1
    print(my_list[a])
    a += 1
