calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(word):
    count_calls()
    string = str(word)
    string1 = (len(string), string.upper(), string.lower())
    return string1
def is_contains(string, list_to_search):
    count_calls()
    for i in range(0, len(list_to_search)):
        if type(list_to_search[i]) != str:
            list_to_search[i] = str(list_to_search[i])
        if string.lower() == list_to_search[i].lower():
            return True
    for i in range(0, len(list_to_search)):
        if string != list_to_search[i]:
            return False
    string = str()
    list_to_search = []

print(string_info('barakuda'))
print(string_info('ViCtOrY'))
print(is_contains('1', ['bax', 1, 'BEST', 'tesT']))
print(is_contains('ok', ['OK', 'eng', 'rules']))
print(is_contains('oklic', ['gg', 1, True, 'оkLIK'])) # в строке и списке "о" на разной раскладке
print(calls)

