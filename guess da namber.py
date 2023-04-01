import random


rand = random.randint(0,100)
number = int(input('Введите число от 0 до 100:'))
flag = True

while flag:
    if number < 0 or number > 100:
        print('Еблан, тебе сказали от нуля до ста')
        number = int(input('Введите число от 0 до 100:'))
    else:
        if number > rand:
            print('Меньше')
            number = int(input('Введите число от 0 до 100:'))
        elif number < rand:
            print('Больше')
            number = int(input('Введите число от 0 до 100:'))
        elif number == rand:
            print('Угадал')
            flag = False
        