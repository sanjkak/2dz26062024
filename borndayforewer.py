while True:
    vopros = input('В каком году родился А.С. Пушкин? ')
    if not vopros.isdigit():
        print('Нужно ввести цифрами ')
    else:
        vopros = int(vopros)
        if vopros == 1799:
            print('Правильно! Следующий вопрос ')
            while True:
                day = input('День рождения А.С. Пушкина ')
                if not day.isdigit():
                    print('Нужно ввести цифрами ')
                else:
                    day = int(day)
                    if day == 6:
                        print('Правильно! Экзамен сдан! ')
                        break
                    else:
                         print('Напряги мозги, ты точно знаешь ')
            break
        else:
            print('Подумай получше ')