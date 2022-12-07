"""Игра угадай число меньше чем за 20 попыток"""
import numpy as np
def random_predict(number:int=1)-> int:
    """Рандомно угадываем число
     Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 0
    minnumber=1
    maxnumber=101
    
    while True:
        count+=1
        predict_number = np.random.randint(minnumber, maxnumber)
        if number == predict_number:
            break # выход из цикла, если угадали
        elif (predict_number > number):
            maxnumber=predict_number + 1 
        else:
            minnumber=predict_number
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток"""
    
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number)) #добавляем число в список

    score = int(np.mean(count_ls)) # находим среднее количество попыток
    if score > 20:
        print(f'Ваш алгоритм потратил больше чем 20 попыток')
    else:
        print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score
# RUN
if __name__ == '__main__':
    score_game(random_predict)
