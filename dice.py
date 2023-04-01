import random


input('Симулятор бросков кости, нажмите ВВОД чтобы бросить')
print('Выпало число ' + str(random.randint(1,6)))
choose = input('Бросить еще раз? Да/Нет ')

flag = True

while flag:
    if choose.lower() == 'да':
        print('Выпало число ' + str(random.randint(1,6)))
        choose = input('Бросить еще раз? Да/Нет ')
    else:
        flag = False


