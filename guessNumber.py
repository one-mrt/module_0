import numpy as np

"""
count = 0 # Счетчик попыток
number = np.random.randint(1,101)   # Загадали число
print("Загадано число от 1 до 100")

while True:
    predict = int(input())
    count += 1  # Попытки
    
    if number == predict:   # Выходим если угадали
        break
    elif number > predict:  # 
        print(f"Угадываем число больше {predict}")
    elif number < predict:
        print(f"Угадываемое число меньше {predict}")

print(f"Вы угадали число {number} за {count} попыток.")

"""

number = np.random.randint(1,101)
print("Загадано число от 1 до 100")
for count in range(1,101):
    if number == count:
        break;
print(f"Вы угадали число {number} за {count} попыток.")

def game_core_v1(number):
    '''
        Просто угадываем на random, никак не используя информацию о больше
        или меньше. Функция принимает загадонное число и возвращает число
        попыток
    '''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1,101)
        if number == predict:
            return count

def score_game(game_core):
    '''
        Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    '''
    np.random.seed(1)
    count_ls = []
    random_array = np.random.randint(1,101,size=(1000))

    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score

def game_core_v2(number):
    '''
        Сначала устанавливаем любое число, а потом уменьшаем или увеличиваем
        его в зависимости от того, больше оно или меньше нужного.
        Функция принимает загаданное число и возвращает число попыток
    '''

    count = 1
    predict = np.random.randint(1,101)

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
        
    return count

score_game(game_core_v1)

score_game(game_core_v2)