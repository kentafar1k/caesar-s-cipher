eng = 'abcdefghijklmnopqrstuvwxyz'
rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

eng_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

text = input('Введите текст,с которым работаем: ')
print('Что делаем? шифрование: "s", дефифрование: "d"')
answer1 = input().lower()
print('Какой язык используем? Русский: "ru", Английский: "eng"')
answer2 = input().lower()
answer3 = int(input('Введите шаг сдвига: '))
itog = ''
if answer1 == 's':
    if answer2 == 'ru':
        for c in text:
            if c not in rus and c not in ru_upper:
                itog += c
            elif c in ru_upper:
                ind = ru_upper.find(c) + answer3
                if ind > 31:
                    ind = ind - 32
                itog += ru_upper[ind]
            else:
                ind = rus.find(c) + answer3
                if ind > 31:
                    ind = ind - 32
                itog += rus[ind]
    if answer2 == 'eng':
        for c in text:
            if c not in eng and c not in eng_upper:
                itog += c
            elif c in eng_upper:
                ind = eng_upper.find(c) + answer3
                if ind > 25:
                    ind = ind - 26
                itog += eng_upper[ind]
            else:
                ind = eng.find(c) + answer3
                if ind > 25:
                    ind = ind - 26
                itog += eng[ind]
elif answer1 == 'd':
    if answer2 == 'ru':
        for c in text:
            if c not in rus and c not in ru_upper:
                itog += c
            elif c in ru_upper:
                ind = ru_upper.find(c) - answer3
                if ind < 0:
                    ind = ind + 32
                itog += ru_upper[ind]
            else:
                ind = rus.find(c) - answer3
                if ind < 0:
                    ind = ind + 32
                itog += rus[ind]
    if answer2 == 'eng':
        for c in text:
            if c not in eng and c not in eng_upper:
                itog += c
            elif c in eng_upper:
                ind = eng_upper.find(c) - answer3
                if ind < 0:
                    ind = ind + 26
                itog += eng_upper[ind]
            else:
                ind = eng.find(c) - answer3
                if ind < 0:
                    ind = ind + 26
                itog += eng[ind]

print(itog)
# comment for github
