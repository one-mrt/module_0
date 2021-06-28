import numpy as np

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