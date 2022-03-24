user_name = input('Привет! Предлагаю проверить свои знания английского!  Расскажи, как тебя зовут! ')

print(f'Привет, {user_name}!')

user_score = 0
right_answers = 0

print('Lets begin!')

user_answer = input('My name ___ Vova ')

if user_answer == 'is':
  print('Ответ верный!')
  print('Вы получаете 10 баллов!')
  user_score += 10
  right_answers += 1
else:
  print('Неправильно.')
  print('Правильный ответ: is')

user_answer = input('I ___ a coder. ')

if user_answer == 'am':
  print('Ответ верный!')
  print('Вы получаете 10 баллов!')
  user_score += 10
  right_answers += 1
else:
  print('Неправильно.')
  print('Правильный ответ: am')

user_answer = input('I live ___ Moscow. ')

if user_answer == 'in':
  print('Ответ верный!')
  print('Вы получаете 10 баллов!')
  user_score += 10
  right_answers += 1
else:
  print('Неправильно.')
  print('Правильный ответ: in')

right_percentage = round((right_answers / 3) * 100, 2)

print(f'Вот и все, {user_name}!')
print(f'Вы ответили на {user_score} вопросов из 3 верно.')
print(f"Вы заработали {user_score} баллов")
print(f'Это {right_percentage} процентов.')
