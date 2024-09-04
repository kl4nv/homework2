def custom_write(file_name, strings):
    string_position = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(0, len(strings)):
        tell = file.tell()
        file.write(f'{strings[i]}\n')
        string_position[i + 1, tell] = f'{strings[i]}'
    file.close()
    return string_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)