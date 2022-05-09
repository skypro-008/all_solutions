from utils import load_questions, build_statistics

def main():

    # Получаем список всех вопросов
    questions = load_questions()

    # Считаем количество вопросов
    questions_count = len(questions)

    # Запускаем все вопросы по очереди
    for question in questions:

        # Выводим вопрос
        print(f"{question.build_question()}")

        # Получаем у пользователя ответ
        print("Ответ: ")
        user_input = input().lower()

        # Обновляем информацию
        question.user_answer = user_input
        question.is_asked = True

        # Выводим статистику
        print(question.build_feedback())

    # Благодарим и прощаемся
    print()
    print("Вот и всё!")

    # Выводим финальную статистику
    print(build_statistics(questions))


if __name__ == '__main__':
    main()
