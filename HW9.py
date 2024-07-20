numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 14, 15]
list1 = []
list2 = []
for i in numbers:
    is_prime = True
    if i <= 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime == True:
        list1.append(i)
    else:
        list2.append(i)
print(list1)
print(list2)
