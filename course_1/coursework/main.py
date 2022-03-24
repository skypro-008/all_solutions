import random

alphabet = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "!": "-.-.--",
        "-": "-....-",
        "/": "-..-.",
        "@": ".--.-.",
        "(": "-.--.",
        ")": "-.--.-"
    }
words = ["code", "bit", "list", "soul", "next"]
user_answers = []

def get_random_word_from_list(words):
    """ Получает случайное слово из списка, слова могут повторяться"""
    random.shuffle(words)
    return words[0]


def morse_encode(word):
    """ кодирует слово"""
    new_word = ""
    for symbol in word:
        new_word += alphabet.get(symbol)
        new_word += '  '

    return new_word


def print_statistics(answers):
    """ Распечатывает статистику """
    print()
    print(f"Всего задачек:{len(answers)}")
    print(f"Отвечено верно:{answers.count(True)}")
    print(f"Отвечено неверно:{answers.count(False)}")


if __name__ == '__main__':

    print("Сегодня мы потренируемся расшифровывать морзянку.")
    print("Нажмите Enter и начнем")
    input()

    for _ in range(len(words)):

        word = get_random_word_from_list(words)
        word_encoded = morse_encode(word)
        print(word_encoded)

        print("Введите ваш ответ")
        user_input = input()

        if user_input == word:
            print(f"Верно, {word}!")
            user_answers.append(True)
        else:
            print(f"Неверно, {word}!")
            user_answers.append(False)

    print_statistics(user_answers)
