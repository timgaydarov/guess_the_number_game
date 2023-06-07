from random import randint

'''Генерирует случайное число'''
num = randint(1, 100)

'''Счетчик количества попыток'''
counter = 0

while True:
    user_num = input('Я загадал число от 1 до 100, угадай его: ')
    if not user_num.isdigit():
        print('Можно ввести только числовое значение')
    else:
        user_num = int(user_num)
        counter += 1
        if user_num == num:
            print(f'Ты угадал! Количество попыток: {counter}')
            new_game = input('Хочешь сыграть еще? (y/n) ')
            if new_game == 'y':
                num = randint(1, 100)
                counter = 0
            else:
                print('Спасибо за игру!')
                break
        elif user_num > num:
            print(f"Загаданное число меньше. Попробуй еще раз!")
        else:
            print(f"Загаданное число больше. Попробуй еще раз!")


