while True:
    n = int(input("Введите число с первого камня (вставки): "))
    result = []
    if 3 <= n <= 20:
        for i in range(1, n):
            for j in range(i, n):
                if n % (i + j) == 0 and i != j:
                    result.append([i, j])
        result = str(result)
        a = result.replace(',', '')
        b = a.replace(' ', '')
        c = b.replace('[', '')
        d = c.replace(']', '')
        print(d)
    else:
        print('Число должно быть в диапазоне от 3 до 20')

