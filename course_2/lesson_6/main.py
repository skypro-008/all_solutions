import functions


def main():
    user_score = 0
    print('Введите ваше имя:')
    user_name = input()

    list_of_words = functions.load_words_from_file('words.txt')

    for word in list_of_words:

        word_shuffled = functions.shuffle_word(word)

        print(f'Угадайте слово: {word_shuffled}')
        print('Ваш ответ: ')
        user_input = input().lower()

        if user_input == word:
            print('Верно! Вы получаете 10 очков.')
            user_score += 10
        else:
            print(f'Неверно! Верный ответ – {word}.')

    functions.save_records_to_file('history.txt', user_name, user_score)

    history_data = functions.read_top('history.txt')

    print()
    print(f'Всего игр сыграно: {history_data["count"]}')
    print(f'Максимальный рекорд: {history_data["max"]}')


main()
