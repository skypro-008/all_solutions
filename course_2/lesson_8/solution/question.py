class Question:

    def __init__(self, question, difficulty, right_answer):

        self.question = question
        self.difficulty = difficulty
        self.right_answer = right_answer

        self.is_asked = False
        self.user_answer = None
        self.score = difficulty * 10


    def __repr__(self):
        return f"\
        \nВопрос: {self.question}\
        \nСложность: {self.difficulty}/5\
        \nВерный ответ: {self.right_answer}\
        \nЗадан ли вопрос: {self.is_asked}\
        \nОтвет пользователя: {self.user_answer}\
        \nБаллы за вопрос: {self.score}"

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.score

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответом иначе False.
        """
        return self.right_answer == self.user_answer

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f"Вопрос: {self.question}\nСложность: {self.difficulty}/5"

    def build_feedback(self):
        """Возвращает:
        Ответ верный, получено __ баллов
        Ответ неверный, верный ответ __
        """
        if self.is_correct():
            return f"Ответ верный, получено {self.score} баллов"
        return f"Ответ неверный, верный ответ: {self.right_answer}"

