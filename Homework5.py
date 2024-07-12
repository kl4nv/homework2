immutable_var = 1, 2, 'ok'
print(immutable_var)
# immutable_var[0] = 5 При замене 1го элемента кортежа, выдает ошибку. Элементы кортежа нельзя заменять и удалять
mutable_list = [4,5,6]
mutable_list[0] = 7
mutable_list[1] = 8
print(mutable_list)

