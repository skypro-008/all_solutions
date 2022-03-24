words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

# уровни результатов студента

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

# словарь, где хранятся правильные и неправильные слова

answers = {}

print("Выберете уровень сложности: ")
print("легкий, средний, сложный")

level = input().lower()
levels_dict = {"легкий": words_easy,
               "средний": words_medium,
               "сложный": words_hard,
               }
word = levels_dict[level]

for key, value in word.items():
    print(f"{key}, {len(value)} букв, начинается на {value[0]}")
    answer = input().lower()
    if answer == value:
        print(f"Верно, {key} - это {value}.")
    else:
        print(f"Неверно. {key} - это {value}")

    answers[key] = answer == value

true_answers_count = 0

print("Правильно отвеченные слова:")
for word, result in answers.items():
    if result is True:
        true_answers_count += 1
        print(word)

print("Неправильно отвеченные слова:")
for word, result in answers.items():
    if result is False:
        print(word)

player_range = levels[true_answers_count]

print(f"Ваш ранг: {player_range}")
