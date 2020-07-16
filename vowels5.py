vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Informe a palavra: ")
found = {}

for letter in word:
    if letter in vowels:
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'Foi encontrada', v, 'time(s).')
