questions = ['My name ___  Vova ', 'I ___ a coder ', 'I live ___ Moscow ', ]
answers = ['is', 'am', 'in', ]

user_score = 0  # кол-во заработнанных очков
answered_questions = 0  # кол-во верных ответов
total_questions = 0  # кол-во заданных вопросов
right_percentage = 0  # процент верных ответов
earned_score = 3  # заработанные очки за один ответ
ending = ''

if len(questions) <= len(answers):
    total_questions = len(questions)
else:
    total_questions = len(answers)

while True:
    is_start = input('Привет! Предлагаю проверить свои знания английского! Набери "ready", чтобы начать! ')
    if is_start == 'ready':
        break
    print("Кажется, вы не хотите играть. Очень жаль.")

for question_index in range(total_questions):
    user_answer = input(questions[question_index])
    earned_score = 3
    while True:
        if user_answer == answers[question_index]:
            print('Ответ верный!')
            user_score += earned_score
            answered_questions += 1
            break
        else:
            earned_score -= 1
            if earned_score == 0:
                print(f'Неправильно. Правильный ответ: {answers[question_index]}')
                break
            else:
                print(f'Осталось попыток: {earned_score}, попробуйте еще раз!')
                user_answer = input()

right_percentage = round((user_score / total_questions) * 100, 2)

if 11 <= answered_questions <= 20:
    ending = 'вопросов'
elif answered_questions % 10 == 1:
    ending = 'вопрос'
elif 2 <= answered_questions % 10 <= 4:
    ending = 'вопроса'
else:
    ending = 'вопросов'

print(
    f'от и все! Вы ответили на {answered_questions} {ending} из {total_questions} верно и заработали {user_score} очков')
