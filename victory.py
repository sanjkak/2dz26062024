#Бенджамин Франклин 1706
#товарищ Сталин 1878
#Берия 1899
#Столыпин 1862
#Абрахам Линкольн 1809
vopr = 5
total_vopros = 5
correct_vopros = 0
print('Привет, давай поиграем в небольшую игру. Поехали! ')


while True:
    vopros1 = int(input('В каком году родился Бенджамин Франклин '))
    if vopros1 == 1706:
        correct_vopros += 1
    total_vopros -=1
    vopros2 = int(input('В каком году родился товарищ Сталин '))
    if vopros2 == 1878:
        correct_vopros += 1
    total_vopros -= 1
    vopros3 = int(input('В каком году родился товарищ Берия '))
    if vopros3==1899:
        correct_vopros += 1
    total_vopros -= 1
    vopros4 = int(input('В каком году родился Столыпин '))
    if vopros4 ==1862:
        correct_vopros += 1
    total_vopros -= 1
    vopros5 = int(input('В каком году родился Абрахам Линкольн '))
    if vopros5 ==1809:
        correct_vopros += 1
    total_vopros -= 1

    print(total_vopros)

    print('Количество правильных ответов:', correct_vopros)
    print('Количество ошибок',  vopr - correct_vopros)
    print('Процент правильных ответов', correct_vopros * 100 / vopr)
    print('Процент неправильных ответов', (vopr - correct_vopros) * 100 / vopr)

    ans = str(input("Хочешь начать игру сначала? (да/нет): "))
    if ans == 'нет':
        break


