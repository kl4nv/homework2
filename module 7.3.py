class WordsFinder:
    def __init__(self, *file):
        self.file_names = file

    def get_all_words(self):
        list_p = [',', '.', '=', '!', '?', ';', ':', ' - ']
        dict_words = {}
        for name in self.file_names:
            list_words = [] #список для слов каждого файла
            file_name = name
            with open(file_name, encoding='utf-8') as file:
                # список из слов файла в нижнем регистре с разбивкой по пробелам:
                list_words += file.read().lower().split()
                for i in range(0, len(list_words)):
                    for p in list_p:
                        if p in list_words[i]: #если пунктуация в слове из списка
                            list_words[i] = list_words[i].replace(p, '') #удаляем эту пунктуацию
            dict_words[name] = list_words
        return dict_words

    def find(self, word):
        word = word.lower()
        dict_find = {}
        for name, words in self.get_all_words().items():
            for i in range(0, len(words)):
                if word == words[i]:
                    dict_find[name] = i + 1
        return dict_find

    def count(self, word):
        word = word.lower()
        dict_count = {}
        count = 0
        for name, words in self.get_all_words().items():
            for i in words:
                if i == word:
                    count += 1
            dict_count[name] = count
        return dict_count


finder2 = WordsFinder('test.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего