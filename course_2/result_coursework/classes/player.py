class Player:
    """ Это класс хранит информацию об игроке """

    def __init__(self, name):
        self.name = name
        self.used_words = []

    def get_used_words(self):
        """ Возвращает все использованные слова"""
        return len(self.used_words)

    def add_word(self, word):
        """ Добавляет слово в список использованных слов у пользователя """
        self.used_words.append(word)

    def check_word_is_new(self, word):
        """ Проверяет, не было ли слово использовано """
        if word not in self.used_words:
            return True
        return False

    def count_used_words(self):
        """ Возврашает количество испольщзованных слов"""
        return len(self.used_words)
