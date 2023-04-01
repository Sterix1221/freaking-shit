import random


symbol_user_2 = 0

flag = True


while flag:
    symbol_user = input('Выберите - Камень, Ножницы, или Бумагу: ')
    symbol_comp = random.randint(0,2)
    if symbol_user.lower() == 'камень':
        symbol_user_2 = 0
    elif symbol_user.lower() == 'ножницы':
        symbol_user_2 = 1
    elif symbol_user.lower() == 'бумага':
        symbol_user_2 = 2
    else:
        print('Неверный выбор')
        break


    if symbol_user_2 == symbol_comp:
        print('Ничья, компьютер выбрал ' + symbol_user.lower())
    elif symbol_user_2 == 0 and symbol_comp == 1:
        print('Вы выиграли')
    elif symbol_user_2 == 0 and symbol_comp == 2:
        print('Вы проебали')
    elif symbol_user_2 == 1 and symbol_comp == 0:
        print('Вы проебали')
    elif symbol_user_2 == 1 and symbol_comp == 2:
        print('Вы выиграли')
    elif symbol_user_2 == 2 and symbol_comp == 0:
        print('Вы выиграли')
    elif symbol_user_2 == 2 and symbol_comp == 1:
        print('Вы проебали')
    break