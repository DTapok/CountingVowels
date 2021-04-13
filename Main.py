word = input('Введите слово - ')
dict = {'a': 0, 'o': 0, 'u': 0, 'i': 0, 'e': 0, 'y': 0}
for i in word:
    if i in dict:
        dict[i] = dict[i]+1
print(dict)