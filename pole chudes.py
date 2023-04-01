import random
words = ['Кант', 'Хроника', 'Свинья', 'Вес', 'Кафель', 'Знак', 'Фильтр', 'Башня']


rand = random.randint(0,7)

word = words[rand]
word = word.lower()

not_solved = True

solving = []

solve = ''

for i in range(len(word)):
        solving.append('-')
solve = solve.join(solving)
while not_solved:
    print('Угадайте слово вводя буквы')
    
    
    print(solve)
    while '-' in solve:
        solve = solve.join(solving)
        letter = input('Введите букву:')
        if letter in word:
            print('Такая буква есть')
            ind = word.index(letter)
            solving[ind] = letter
            solve = ''
            solve = solve.join(solving)
            print(solve)
        else:
            print('Этой буквы нету')
            continue
    print('Победа')
    not_solved = False

