from random import randint
import keyboard
print('Отгадыватель мыслей')
print('~~~~~~~~~~~~~~~~~~~')
print()
print('Задумайте двузначное число.')
print('Вычтите из него сумму его цифр. Разность запомните.')
print('Если вы готовы - нажмите клавишу \"пробел\" и найдете эту разность в появившейся таблице, '
      'и запомните символ справа от неё.')
keyboard.wait("space")
t = [[0] * 100 for _ in range(100)]
for i in range(1 , 11):
    for j in range(1, 21):
        t[i][2 * j - 1] = str(10 * (i - 1) + (j - 1) + 0)
for i in range(1, 11):
    for j in range(1, 21):
        r = 150 + randint(1, 105)
        t[i][2 * j] = chr(r)
r = 150 + randint(1, 105)
z = chr(r)
for i in range(1, 11):
    for j in range(1, 21):
        if int(t[i][2 * j - 1]) % 9 == 0:
            t[i][2 * j] = z
print()
for i in range(1, 11):
    for j in range(1, 21):
        print("{:>3}".format(t[i][j]), end=' ')
    print()
print()
print('Если вы нашли \"свой\" символ, нажмите клавишу \"пробел\"')
keyboard.wait("space")
print()
print(f'Ваша мысль угадана! Вы нашли символ "{z}" - Невероятно!')