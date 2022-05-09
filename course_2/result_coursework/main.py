from classes.basic_word import BasicWord
from classes.player import Player
from utils import load_random_word

print("Введите имя игрока")
name = input()

player = Player(name=name)

original_word = load_random_word()
subwords_count = original_word.count_species()

print(f"Привет, {player.name}!")
print(f"Составьте {subwords_count} слов из слова {original_word.initial_word.upper()}")
print(f"Слова должны быть не короче 3 букв")
print(f"Поехали! Ваше первое слово?")

while player.count_used_words() < subwords_count:

    word = input().lower()

    if word == "stop":
        break

    if len(word) < 3:
        print("Слово какое-то короткое, уходи")
        continue

    if original_word.check_word(word) and player.check_word_is_new(word):
        print("Такое слово есть!")
        player.add_word(word)
    else:
        print("Такого слова нет или оно было использовано!")

print(f"Игра закончена! Вы угадали {player.get_used_words()} слов(а)")
