a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))
if a==b==c:
    print(3)
elif a==b or a==c or b==c:
    print(2)
else: print(0)