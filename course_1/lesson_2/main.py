# Задаем основные переменные

user_score = 0
right_answers = 0

# Здороваемся с пользователем

print('Привет! Предлагаю проверить свои знания английского!')
print('Расскажи, как тебя зовут!')
user_name = input()
print(f'Привет, {user_name}!')
print('Lets begin!')

# Задаем первый вопрос

user_answer = input('My name ___ Vova ')

if user_answer == 'is':
    print('Ответ верный!')
    print('Вы получаете 10 баллов!')
    right_answers += 1
else:
    print('Неправильно.')
    print('Правильный ответ: is')

# Задаем второй вопрос

user_answer = input('I ___ a coder. ')

if user_answer == 'am':
    print('Ответ верный!')
    print('Вы получаете 10 баллов!')
    user_score += 10
    right_answers += 1
else:
    print('Неправильно.')
    print('Правильный ответ: am')

# Задаем третий вопрос

user_answer = input('I live ___ Moscow. ')

if user_answer == 'in':
    print('Ответ верный!')
    print('Вы получаете 10 баллов!')
    user_score += 10
    right_answers += 1
else:
    print('Неправильно.')
    print('Правильный ответ: in')

# Посчитаем статистику теперь

user_score = right_answers * 10
right_percentage = round((right_answers / 3) * 100, 2)

# Выведем статистику

print(f'Вот и все, {user_name}!')
print(f'Вы ответили на {user_score} вопросов из 3 верно.')
print(f"Вы заработали {user_score} баллов")
print(f'Это {right_percentage} процентов.')
