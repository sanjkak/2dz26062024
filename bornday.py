while True:
    vopros = input('В каком году родился А.С. Пушкин? ')
    if not vopros.isdigit():
        print('Нужно ввести цифрами')
    else:
        vopros = int(vopros)
        if vopros == 1799:
            print('Правильно!')
            break
        else:
            print('Подумай получше')