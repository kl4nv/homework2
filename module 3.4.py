def single_root_words(root_word='Hellobe', *other_words):
    root_word = root_word.lower()
    same_words = []
    for i in range(len(other_words)):
        other_words1 = [j.lower() for j in other_words]
        if root_word in other_words1[i]:
            same_words.append(other_words[i])
        if other_words1[i] in root_word:
            same_words.append(other_words[i])
    return same_words



result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)